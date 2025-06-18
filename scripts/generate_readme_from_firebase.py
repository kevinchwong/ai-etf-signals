#!/usr/bin/env python3
import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict
from dotenv import load_dotenv
import pytz
import openai
import firebase_admin
from firebase_admin import credentials, firestore

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


load_dotenv()

# Constants
REQUIRED_ENV_VARS = ['GCP_SA_KEY', 'FIREBASE_PROJECT_ID', 'FIREBASE_ETF_ANALYSIS_COLLECTION', 'DEEPSEEK_API_KEY']
DEFAULT_TIMEOUT = 30
MAX_REDIRECTS = 5
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

def validate_environment_vars():
    """Validate that all required environment variables are set."""
    missing_vars = []
    malformed_vars = []
    
    for var in REQUIRED_ENV_VARS:
        value = os.environ.get(var)
        if not value:
            missing_vars.append(var)
        elif var == 'GCP_SA_KEY':
            try:
                json.loads(value)
            except json.JSONDecodeError:
                malformed_vars.append(var)
    
    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        logger.error("Please set these environment variables or create a .env file")
        logger.error("See env_template.txt for reference")
    
    if malformed_vars:
        logger.error(f"Malformed environment variables: {', '.join(malformed_vars)}")
        logger.error("Please check the format of these variables")
        logger.error("For GCP_SA_KEY, ensure it's valid JSON")
    
    if missing_vars or malformed_vars:
        raise EnvironmentError(f"Environment validation failed. Missing: {missing_vars}, Malformed: {malformed_vars}")
    
def initialize_firebase():
    """Initialize Firebase with proper error handling."""
    try:
        validate_environment_vars()
        
        # Get the service account key and validate it
        gcp_sa_key = os.environ['GCP_SA_KEY']
        logger.info(f"GCP_SA_KEY length: {len(gcp_sa_key)} characters")
        
        try:
            service_account_info = json.loads(gcp_sa_key)
            logger.info("Successfully parsed GCP service account key")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse GCP_SA_KEY as JSON: {e}")
            logger.error(f"GCP_SA_KEY starts with: {gcp_sa_key[:100]}...")
            logger.error(f"GCP_SA_KEY ends with: ...{gcp_sa_key[-100:]}")
            raise
        
        cred = credentials.Certificate(service_account_info)
        firebase_admin.initialize_app(cred)
        logger.info("Firebase app initialized successfully")
        return firestore.client()
    except Exception as e:
        logger.error(f"Error initializing Firebase: {str(e)}")
        raise

def clean_and_get_latest_signal_from_firebase(db):
    """Clean and get the latest signal from Firebase."""
    try:
        collection_ref = db.collection(os.environ['FIREBASE_ETF_ANALYSIS_COLLECTION'])
        etf_signals = list(collection_ref.stream())
        
        if not etf_signals:
            logger.info("No ETF signals found in Firebase collection")
            return None
        
        logger.info(f"Found {len(etf_signals)} ETF signals in Firebase")
        
        # Sort by updated_on in descending order with better error handling
        def get_updated_on(signal):
            try:
                data = signal.to_dict()
                updated_on = data.get('updated_on')
                if updated_on is None:
                    logger.warning(f"Signal {signal.id} has no updated_on field, using timestamp 0")
                    return 0
                
                # Handle different types of updated_on values
                if isinstance(updated_on, (int, float)):
                    return float(updated_on)
                elif hasattr(updated_on, 'timestamp'):
                    # Handle datetime objects
                    return updated_on.timestamp()
                elif isinstance(updated_on, str):
                    # Handle datetime strings (ISO format)
                    try:
                        dt = datetime.fromisoformat(updated_on.replace('Z', '+00:00'))
                        return dt.timestamp()
                    except ValueError:
                        logger.warning(f"Could not parse datetime string '{updated_on}' for signal {signal.id}, using timestamp 0")
                        return 0
                else:
                    logger.warning(f"Unknown updated_on type {type(updated_on)} for signal {signal.id}, using timestamp 0")
                    return 0
            except Exception as e:
                logger.warning(f"Error getting updated_on for signal {signal.id}: {e}")
                return 0
        
        etf_signals.sort(key=get_updated_on, reverse=True)
        
        # Get the latest signal
        latest_etf_signal = etf_signals[0].to_dict()
        logger.info(f"Latest signal timestamp: {latest_etf_signal.get('updated_on', 'unknown')}")
        
        # Delete old signals with better error handling
        if len(etf_signals) > 1:
            logger.info(f"Deleting {len(etf_signals) - 1} old signals")
            deleted_count = 0
            for signal in etf_signals[1:]:
                try:
                    signal.reference.delete()
                    deleted_count += 1
                except Exception as e:
                    logger.error(f"Error deleting signal {signal.id}: {e}")
            
            logger.info(f"Successfully deleted {deleted_count} old signals")
        
        return latest_etf_signal
        
    except Exception as e:
        logger.error(f"Error retrieving latest signal from Firebase: {str(e)}")
        raise

def ask_llm_to_generate_readme_content(latest_etf_signal:Dict)->str:
    """Ask the LLM to generate the README.md content."""
    # Set DeepSeek API key from environment
    openai.api_key = os.environ.get('DEEPSEEK_API_KEY')
    
    if not openai.api_key:
        raise EnvironmentError("DEEPSEEK_API_KEY environment variable is not set")
    
    prompt = f"""

    Plan me hour by hour ETF options strategy for today from now to 4pm EST with the following prediction data:
    {latest_etf_signal}
    
    Must include current EST time in the header.
    Output in markdown format.
    """
    
    try:
        client = openai.OpenAI(
            api_key=os.environ.get('DEEPSEEK_API_KEY'),
            base_url="https://api.deepseek.com",
        )    
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an elite quantitative trader specializing in ETF momentum strategies. return report in markdown format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=4096,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        # current_est_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")
        readme_src = "\n".join(response.choices[0].message.content[:-3].split("\n")[1:-1])
        return (
            f"{readme_src}\n\n" +
            f"Signal data: ```{latest_etf_signal}```"
        )
        
    except Exception as e:
        logger.error(f"Error calling DeepSeek API: {str(e)}")
        raise

def generate_readme_content(db):
    """Generate the README.md content from the latest ETF signal."""
    current_est_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")
    
    logger.info("Retrieving latest ETF signal from Firebase")
    latest_etf_signal = clean_and_get_latest_signal_from_firebase(db)
    
    if latest_etf_signal is not None:
        
        logger.info("Generating README content using LLM")
        try:
            # readme_content = ask_llm_to_generate_readme_content(latest_etf_signal)
            readme_content = f"## Signal data\n\n" + \
                f"{latest_etf_signal['updated_on']}\n\n" + \
                f"{latest_etf_signal['summary']}\n\n" + \
                f"{latest_etf_signal['tabulate_sells']}\n\n" + \
                f"{latest_etf_signal['tabulate_buys']}\n\n" + \
                f"{latest_etf_signal['tabulate_etfs']}\n\n"
            logger.info("Successfully generated README content from LLM")
            return readme_content
        except Exception as e:
            logger.error(f"Failed to generate content from LLM: {e}")
            logger.info("Falling back to default content")
            
    return f"""# AI ETF Signals

Latest signal data available at {current_est_time} EST.

Signal data: {latest_etf_signal}

Please check back later for updated ETF options strategies.
"""

def update_readme(content):
    """Update the README.md file."""
    try:
        with open("README.md", "w") as f:
            f.write(content)
            logger.info("README.md has been updated successfully!")
    except Exception as e:
        logger.error(f"Error updating README.md: {str(e)}")
        raise

def main():
    """Main function to generate README from Firebase data."""
    try:
        logger.info("Starting README generation from Firebase data")
        
        # Initialize Firebase
        logger.info("Initializing Firebase connection")
        db = initialize_firebase()
        logger.info("Firebase connection established successfully")
        
        # Generate README content
        logger.info("Generating README content")
        readme_content = generate_readme_content(db)
        logger.info(f"Generated README content with size: {len(readme_content)} characters")
        
        # Update README file
        logger.info("Updating README.md file")
        update_readme(readme_content)
        
        logger.info("README generation completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        logger.error(f"Error type: {type(e).__name__}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == "__main__":
    main() 