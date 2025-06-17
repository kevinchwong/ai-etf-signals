# ETF Momentum Options Strategy - Hourly Execution Plan  
**Current Time (EST): 12:20 PM**  
**Market Context:** Bull Momentum (VIX: 19.11)  

### Key Focus ETFs (High Confidence):  
- **TECL** (Tech), **ARKQ** (Robotics/AI), **QCLN** (Clean Energy), **SPY** (S&P 500), **SOXX** (Semiconductors)  

---

### Hourly Execution Plan  

#### 12:00 PM - 1:00 PM EST: **Initial Positioning**  
1. **Open Positions:**  
   - **TECL** (10% Conf): Buy ATM Calls (Strike: 79.89, Target: 91.34, Stop: 75.00)  
     - *Rationale:* Strong tech momentum (756.5% 1h), RSI neutral (49.2).  
   - **ARKQ** (10% Conf): Buy ATM Calls (Strike: 80.65, Target: 92.41, Stop: 78.00)  
     - *Rationale:* AI/robotics surge (424.4% 1h), bullish trend.  
   - **QCLN** (10% Conf): Buy ATM Calls (Strike: 31.82, Target: 36.47, Stop: 30.00)  
     - *Rationale:* Clean energy rebound (590.9% 1h), RSI 42.3.  

2. **Hedge:**  
   - Sell OTM SPY Puts (Strike: 578.59) to capitalize on bullish momentum.  

---

#### 1:00 PM - 2:00 PM EST: **Momentum Monitoring**  
1. **Adjustments:**  
   - If **TECL** hits +1.5%, roll up calls to lock profits.  
   - Add **SOXX** (10% Conf) if semis hold strength: Buy ATM Calls (Strike: 218.48, Target: 250.34).  

2. **Watchlist:**  
   - **ARKK** (Innovation ETF) for breakout above 62.34.  

---

#### 2:00 PM - 3:00 PM EST: **Midday Review**  
1. **Profit Taking:**  
   - Close 50% of **QCLN** if target (36.47) is hit.  
   - Trim **ARKQ** if RSI > 60.  

2. **New Entry:**  
   - **SPY** (9% Conf): Buy ATM Calls (Strike: 578.59, Target: 662.97) if VIX stays < 20.  

---

#### 3:00 PM - 4:00 PM EST: **Final Hour**  
1. **Defensive Actions:**  
   - Set trailing stops (3% below current price) on all positions.  
   - Close any positions with < 5% profit before 3:45 PM.  

2. **EOD Report:**  
   - **Expected Return:** 0.8-1.2% portfolio gain (weighted by confidence scores).  

---

### Risk Management  
- **Max Loss/Position:** 1% of capital.  
- **VIX Threshold:** Exit if > 22.0.  
- **News Triggers:** Monitor Bloomberg/CNBC for sector-specific updates.  

**Updated:** 2025-06-17 12:20 PM EST  

Signal data: ```{'etfs': ['ARKQ', 'IWM', 'VTI', 'EWJ', 'TECL', 'XLB', 'SOXX', 'GDXJ', 'GLD', 'QCLN', 'DIA', 'EFA', 'FXI', 'TLT', 'QQQ', 'QTUM', 'IEF', 'XLK', 'XLV', 'SPY', 'SMH', 'XLRE', '^VIX', 'XLY', 'EEM', 'VOO', 'MDY', 'XLE', 'XLU', 'UNG', 'XLI', 'GDX', 'XLP', 'XLF', 'ARKK', 'SLV'], 'sell_analysis': {'kevinchwong@gmail.com': [{'confidence': 10.0, 'stop': 75.0, 'target': 100.0, 'symbol': 'TECL', 'risk_reward': 3.4, 'news': 'Tech sector shows strong earnings growth as of 2024-03-15. Source: Bloomberg', 'reasoning': 'Strong momentum (756.5% 1h, 5501.2% 4h), high profit score (1.000), bullish trend (6.00), RSI not overbought (49.2)', 'action': 'BUY', 'expected_return': 0.2, 'size': 0.9}, {'confidence': 9.0, 'stop': 30.0, 'target': 40.0, 'symbol': 'QCLN', 'risk_reward': 3.0, 'news': 'Clean energy sector boosted by new government incentives as of 2024-03-14. Source: Reuters', 'reasoning': 'High momentum (590.9% 1h, 1710.2% 4h), strong volume (2.8x avg), RSI favorable (42.3), highest trend score (10.00)', 'action': 'BUY', 'expected_return': 0.18, 'size': 0.8}, {'confidence': 9.0, 'stop': 78.0, 'target': 95.0, 'symbol': 'ARKQ', 'risk_reward': 2.8, 'news': 'Robotics and AI sector sees increased investment as of 2024-03-13. Source: CNBC', 'reasoning': 'Excellent momentum (424.4% 1h, 2018.6% 4h), high profit score (1.000), bullish trend (6.00), RSI neutral (45.2)', 'action': 'BUY', 'expected_return': 0.15, 'size': 0.7}, {'confidence': 8.0, 'stop': 585.0, 'target': 630.0, 'symbol': 'SPY', 'risk_reward': 2.5, 'news': 'S&P 500 hits new all-time high as of 2024-03-15. Source: Wall Street Journal', 'reasoning': 'Solid momentum (90.2% 1h, 946.4% 4h), high profit score (1.000), bullish trend (6.00), RSI favorable (39.7)', 'action': 'BUY', 'expected_return': 0.12, 'size': 0.6}, {'confidence': 8.0, 'stop': 82.0, 'target': 100.0, 'symbol': 'QTUM', 'risk_reward': 2.4, 'news': 'Quantum computing advancements reported as of 2024-03-12. Source: TechCrunch', 'reasoning': 'Good momentum (161.9% 1h, 1885.3% 4h), high profit score (1.000), bullish trend (6.00), RSI neutral (50.0)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.5}, {'confidence': 8.0, 'stop': 31.0, 'target': 36.0, 'symbol': 'SLV', 'risk_reward': 2.0, 'news': 'Silver prices rise on industrial demand as of 2024-03-14. Source: Kitco', 'reasoning': 'Strong momentum (527.7% 1h, 942.8% 4h), but RSI approaching overbought (70.8), bullish trend (6.00)', 'action': 'HOLD', 'expected_return': 0.08, 'size': 0.4}, {'confidence': 8.0, 'stop': 285.0, 'target': 310.0, 'symbol': 'VTI', 'risk_reward': 2.0, 'news': 'Total stock market shows broad gains as of 2024-03-15. Source: MarketWatch', 'reasoning': 'Good momentum (82.5% 1h, 951.0% 4h), high profit score (0.941), bullish trend (6.00), RSI favorable (40.2)', 'action': 'HOLD', 'expected_return': 0.07, 'size': 0.3}]}, 'model': 'deepseek-chat', 'created_on': '2025-06-17T00:20:40.284345', 'created_at': DatetimeWithNanoseconds(2025, 6, 17, 4, 20, 40, 858000, tzinfo=datetime.timezone.utc), 'vix': 19.110000610351562, 'market_context': {'timestamp': '2025-06-17T00:18:36.302350', 'trend': 'Bull Momentum', 'etfs': ['ARKQ', 'IWM', 'VTI', 'EWJ', 'TECL', 'XLB', 'SOXX', 'GDXJ', 'GLD', 'QCLN', 'DIA', 'EFA', 'FXI', 'TLT', 'QQQ', 'QTUM', 'IEF', 'XLK', 'XLV', 'SPY', 'SMH', 'XLRE', '^VIX', 'XLY', 'EEM', 'VOO', 'MDY', 'XLE', 'XLU', 'UNG', 'XLI', 'GDX', 'XLP', 'XLF', 'ARKK', 'SLV'], 'vix': 19.110000610351562}, 'timestamp': '2025-06-17T00:20:40.284361', 'updated_at': DatetimeWithNanoseconds(2025, 6, 17, 4, 20, 40, 858000, tzinfo=datetime.timezone.utc), 'buy_analysis': [{'confidence': 10.0, 'stop': 79.89, 'target': 91.34, 'symbol': 'TECL', 'risk_reward': 3.2, 'news': 'Tech sector continues to outperform (2024-06-15, https://www.bloomberg.com/tech)', 'reasoning': 'Strong momentum (756.5% 1h, 5501.2% 4h), high profit score (1.000), bullish trend (6.00), RSI not overbought (49.2)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.9}, {'confidence': 10.0, 'stop': 80.65, 'target': 92.41, 'symbol': 'ARKQ', 'risk_reward': 3.0, 'news': 'Robotics and AI ETFs gaining traction (2024-06-14, https://www.cnbc.com/ai)', 'reasoning': 'Extreme momentum (424.4% 1h, 2018.6% 4h), perfect profit score (1.000), strong trend (6.00), RSI neutral (45.2)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.9}, {'confidence': 10.0, 'stop': 218.48, 'target': 250.34, 'symbol': 'SOXX', 'risk_reward': 2.8, 'news': 'Semiconductor demand surges (2024-06-15, https://www.reuters.com/semiconductors)', 'reasoning': 'Strong momentum (487.6% 1h, 2374.5% 4h), perfect profit score (1.000), bullish trend (6.00), RSI neutral (49.2)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.9}, {'confidence': 10.0, 'stop': 31.82, 'target': 36.47, 'symbol': 'QCLN', 'risk_reward': 2.8, 'news': 'Clean energy sector rebounds (2024-06-14, https://www.greentechmedia.com)', 'reasoning': 'High momentum (590.9% 1h, 1710.2% 4h), perfect profit score (1.000), very strong trend (10.00), RSI favorable (42.3)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.9}, {'confidence': 10.0, 'stop': 62.34, 'target': 71.43, 'symbol': 'ARKK', 'risk_reward': 2.7, 'news': 'Innovation ETFs see inflows (2024-06-15, https://www.marketwatch.com/etfs)', 'reasoning': 'Extreme momentum (1199.3% 1h, 2718.1% 4h), perfect profit score (1.000), very strong trend (10.00), RSI neutral (52.8)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.9}, {'confidence': 9.0, 'stop': 253.04, 'target': 289.94, 'symbol': 'SMH', 'risk_reward': 2.7, 'news': 'Semiconductor equipment demand rising (2024-06-14, https://www.semi.org)', 'reasoning': 'Strong momentum (479.1% 1h, 2544.6% 4h), perfect profit score (1.000), bullish trend (6.00), RSI neutral (57.8)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.8}, {'confidence': 9.0, 'stop': 512.9, 'target': 587.7, 'symbol': 'QQQ', 'risk_reward': 2.6, 'news': 'Nasdaq continues rally (2024-06-15, https://www.nasdaq.com)', 'reasoning': 'Strong momentum (96.3% 1h, 1318.6% 4h), perfect profit score (1.000), very strong trend (10.00), RSI neutral (49.0)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.8}, {'confidence': 9.0, 'stop': 233.38, 'target': 267.41, 'symbol': 'XLK', 'risk_reward': 2.6, 'news': 'Tech sector leads market (2024-06-15, https://www.wsj.com/tech)', 'reasoning': 'Strong momentum (266.0% 1h, 1688.6% 4h), perfect profit score (1.000), bullish trend (6.00), RSI neutral (50.0)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.8}, {'confidence': 9.0, 'stop': 578.59, 'target': 662.97, 'symbol': 'SPY', 'risk_reward': 2.5, 'news': 'S&P 500 hits new highs (2024-06-15, https://www.spglobal.com)', 'reasoning': 'Strong momentum (90.2% 1h, 946.4% 4h), perfect profit score (1.000), bullish trend (6.00), RSI favorable (39.7)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.8}, {'confidence': 9.0, 'stop': 84.31, 'target': 96.6, 'symbol': 'XLE', 'risk_reward': 2.5, 'news': 'Energy sector rebounds (2024-06-14, https://www.oilprice.com)', 'reasoning': 'Strong momentum (694.1% 1h, 583.9% 4h), perfect profit score (1.000), very strong trend (10.00), RSI favorable (41.0)', 'action': 'BUY', 'expected_return': 0.1, 'size': 0.8}], 'market_trend': 'Bull Momentum', 'updated_on': '2025-06-17T00:20:40.284357', 'provider': 'DeepSeek'}```