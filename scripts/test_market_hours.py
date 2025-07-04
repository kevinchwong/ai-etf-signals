#!/usr/bin/env python3
"""
Test script to verify market hours checker functionality.
Run this script to test if the market hours detection is working correctly.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_readme_from_firebase import is_market_open, is_market_trading_day
import pytz
from datetime import datetime

def test_market_hours():
    """Test the market hours checker functions."""
    print("=== Market Hours Checker Test ===\n")
    
    # Test trading day check
    print("1. Testing trading day check:")
    is_trading_day = is_market_trading_day()
    print(f"   Is trading day: {is_trading_day}")
    
    # Get current time in EST
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern)
    print(f"   Current time (EST): {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"   Current day: {current_time.strftime('%A')}")
    
    print("\n2. Testing market open check:")
    is_open = is_market_open()
    print(f"   Is market open: {is_open}")
    
    print("\n3. Combined check:")
    if is_trading_day and is_open:
        print("   ✅ Market is open and it's a trading day - UPDATE SHOULD PROCEED")
    elif is_trading_day and not is_open:
        print("   ⏸️  It's a trading day but market is closed - UPDATE SHOULD BE SKIPPED")
    elif not is_trading_day:
        print("   🚫 It's not a trading day (weekend) - UPDATE SHOULD BE SKIPPED")
    else:
        print("   ❓ Unknown state")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_market_hours() 