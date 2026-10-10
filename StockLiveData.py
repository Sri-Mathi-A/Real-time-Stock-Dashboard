import yfinance as yf
import requests
import datetime
import time
import pandas as pd
import numpy as np
import pytz
from sklearn.linear_model import LinearRegression

# 1. Unga Power BI Push URL
PBI_ENDPOINT = "https://api.powerbi.com/beta/f1a19bfc-8305-4b24-8140-6dcd45d272f4/datasets/9398d9e8-8ff1-4cf2-b1cb-9b3592cb27aa/rows?experience=power-bi&key=aNr0nSKaX%2FTXB3b8d3gqq7Cx1IxNiv%2FnQVxm6o65mg4I9QbG84xQNYkn2mjga3STho3YgYE9MkA8t0kM1fxoew%3D%3D"

tickers = ["AAPL", "TSLA", "NVDA", "MSFT", "AMD", "GOOGL"]
prev_prices = {ticker: 0 for ticker in tickers}


def is_market_open():
    # US Market timings (9:30 AM to 4:00 PM EST)
    est = pytz.timezone('US/Eastern')
    now = datetime.datetime.now(est)
    if now.weekday() >= 5: return False  # Sat/Sun close
    market_start = now.replace(hour=9, minute=30, second=0, microsecond=0)
    market_end = now.replace(hour=16, minute=0, second=0, microsecond=0)
    return market_start <= now <= market_end


def compute_rsi(data, window=14):
    if len(data) < window: return 50
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs)).iloc[-1]


print("📊 Live Quant-Stream Started... Syncing with Market Hours.")

while True:
    market_open = is_market_open()
    status_text = "Open" if market_open else "Closed"

    # --- 🔥 MAIN LOGIC 🔥 ---
    # Market close-ah irundha, namma data anuppa vendaam (No updates)
    if not market_open:
        print(f"😴 Market is CLOSED ({datetime.datetime.now().strftime('%H:%M:%S')}). Waiting...")
        time.sleep(60)  # 1 minute wait panni marupadiyum check pannum
        continue

    # Market open-ah irundha mattum kila irukura loop run aagum
    for symbol in tickers:
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="1d", interval="1m")
            if hist.empty: continue

            latest = hist.iloc[-1]
            current_price = round(float(latest['Close']), 2)
            last_recorded = prev_prices[symbol]

            # Signal Logic (Price fluctuation kaatta)
            if last_recorded == 0:
                signal = 0
            elif current_price > last_recorded:
                signal = 1
            elif current_price < last_recorded:
                signal = -1
            else:
                signal = 0  # Same price-naalum data push aagum (Live update)

            prev_prices[symbol] = current_price
            open_price = float(hist.iloc[0]['Open'])
            pct_change = round(((current_price - open_price) / open_price) * 100, 2)

            payload = [{
                "Symbol": symbol,
                "Price": current_price,
                "Signal": int(signal),
                "PctChange": pct_change,
                "Volume": int(latest['Volume']),
                "RSI": round(float(compute_rsi(hist)), 2),
                "MarketStatus": status_text,
                "DateTime": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
            }]

            requests.post(PBI_ENDPOINT, json=payload)
            print(f"✅ Pushed {symbol}: ${current_price} | Signal: {signal}")

        except Exception as e:
            print(f"⚠️ Error with {symbol}: {e}")

    time.sleep(10)  # 10 seconds refresh