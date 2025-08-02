# macro_bot/finnhub_fetcher.py

import requests
import os

FINNHUB_KEY = os.getenv("FINNHUB_KEY")

def fetch_quote(symbol):
    try:
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_KEY}"
        res = requests.get(url).json()
        return float(res.get("c", 0))  # "c" = current price
    except Exception as e:
        print(f"❌ Finnhub fetch error for {symbol}: {e}")
        return 0.0

def fetch_vix():
    return fetch_quote("^VIX")

def fetch_us10y():
    return fetch_quote("US10Y")

def fetch_dxy():
    return fetch_quote("DXY")
