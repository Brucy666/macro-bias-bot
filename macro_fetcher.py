# macro_fetcher.py

import yfinance as yf
import requests

def get_dxy_change():
    try:
        dxy = yf.Ticker("DX-Y.NYB")  # DXY index symbol
        hist = dxy.history(period="2d")
        if len(hist) >= 2:
            yesterday = hist["Close"].iloc[0]
            today = hist["Close"].iloc[1]
            change = ((today - yesterday) / yesterday) * 100
            return round(change, 2)
    except Exception as e:
        print(f"❌ DXY error: {e}")
    return 0.0

def get_vix():
    try:
        vix = yf.Ticker("^VIX")
        return round(vix.info.get("regularMarketPrice", 0), 2)
    except Exception as e:
        print(f"❌ VIX error: {e}")
    return 0.0

def get_yield_10y():
    try:
        ten_year = yf.Ticker("^TNX")
        return round(ten_year.info.get("regularMarketPrice", 0) / 10, 2)  # TNX is in 10x format
    except Exception as e:
        print(f"❌ US10Y error: {e}")
    return 0.0

def get_bitmex_lsr():
    try:
        # Placeholder for now – replace with Coinglass or webhook later
        return 3.2
    except Exception as e:
        print(f"❌ BitMEX L/S error: {e}")
    return 1.0

def get_macro_data():
    return {
        "dxy_change_1d": get_dxy_change(),
        "vix": get_vix(),
        "us10y": get_yield_10y(),
        "bitmex_lsr": get_bitmex_lsr(),
        "news_sentiment": "neutral"  # placeholder for now
    }
