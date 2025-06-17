#!/usr/bin/env python3
import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict

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

# Constants
REQUIRED_ENV_VARS = ['GCP_SA_KEY', 'FIREBASE_PROJECT_ID', 'FIREBASE_ETF_COLLECTION', 'DEEPSEEK_API_KEY']
DEFAULT_TIMEOUT = 30
MAX_REDIRECTS = 5
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

def validate_environment_vars():
    """Validate that all required environment variables are set."""
    missing_vars = [var for var in REQUIRED_ENV_VARS if not os.environ.get(var)]
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

def initialize_firebase():
    """Initialize Firebase with proper error handling."""
    try:
        validate_environment_vars()
        service_account_info = json.loads(os.environ['GCP_SA_KEY'])
        cred = credentials.Certificate(service_account_info)
        firebase_admin.initialize_app(cred)
        return firestore.client()
    except Exception as e:
        logger.error(f"Error initializing Firebase: {str(e)}")
        raise

def clean_and_get_latest_signal_from_firebase(db):
    """Clean and get the latest signal from Firebase."""
    try:
        collection_ref = db.collection(os.environ['FIREBASE_ETF_COLLECTION'])
        etf_signals = list(collection_ref.stream())
        if not etf_signals:
            return None
        
        # Sort by updated_on in descending order
        etf_signals.sort(key=lambda x: x.to_dict().get('updated_on', 0), reverse=True)
        
        # Get the latest signal
        latest_etf_signal = etf_signals[0].to_dict()
        
        # delete the old signals
        for signal in etf_signals[1:]:
            signal.reference.delete()
        
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
    Give me hour by hour ETF options strategy with the following prediction data:
    {latest_etf_signal}
    output in markdown format.
    """
    
    try:
        response = openai.chat.completions.create(
            model="DeepSeek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error calling DeepSeek API: {str(e)}")
        raise

def generate_readme_content(db):
    """Generate the README.md content from the latest ETF signal with SEO optimization."""
    current_est_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")
    latest_etf_signal = clean_and_get_latest_signal_from_firebase(db)
    
    if latest_etf_signal is None:
        logger.warning("No ETF signals found in Firebase. Generating default README content.")
        return f"""# AI ETF Signals

No signals available at {current_est_time} EST.

Please check back later for updated ETF options strategies.
"""
    
    readme_content = ask_llm_to_generate_readme_content(latest_etf_signal)
    return readme_content


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
        db = initialize_firebase()
        readme_content = generate_readme_content(db)
        logger.info(f"Generated README content with size: {len(readme_content)}")
        update_readme(readme_content)
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 