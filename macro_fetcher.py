# macro_bot/macro_fetcher.py

import requests
import os
import time

FINNHUB_KEY = os.getenv("FINNHUB_KEY")

def fetch_quote(symbol):
    try:
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()
        return round(float(data.get("c", 0)), 2)  # "c" = current price
    except Exception as e:
        print(f"❌ Finnhub fetch error for {symbol}: {e}")
        return 0.0

def fetch_vix():
    return fetch_quote("^VIX")

def fetch_us10y():
    return fetch_quote("US10Y")

def fetch_dxy():
    return fetch_quote("DXY")

def get_bitmex_lsr():
    try:
        # Replace with real Coinglass or webhook integration later
        return 3.2
    except Exception as e:
        print(f"❌ BitMEX L/S fetch error: {e}")
        return 1.0

def get_macro_data():
    return {
        "dxy": fetch_dxy(),
        "vix": fetch_vix(),
        "us10y": fetch_us10y(),
        "bitmex_lsr": get_bitmex_lsr(),
        "news_sentiment": "neutral"  # Placeholder for now
    }
