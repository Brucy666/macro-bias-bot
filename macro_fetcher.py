# macro_fetcher.py

import yfinance as yf
import time

def get_vix():
    try:
        time.sleep(1)  # Avoid 429 rate limit
        vix = yf.Ticker("^VIX")
        return round(vix.info.get("regularMarketPrice", 0), 2)
    except Exception as e:
        print(f"❌ VIX error: {e}")
        return 0.0

def get_yield_10y():
    try:
        time.sleep(1)
        tnx = yf.Ticker("^TNX")  # US 10-Year Yield Index
        return round(tnx.info.get("regularMarketPrice", 0) / 10, 2)  # Divide by 10 to convert format
    except Exception as e:
        print(f"❌ US10Y error: {e}")
        return 0.0

def get_dxy_change():
    try:
        # TEMPORARILY DISABLED (DX-Y.NYB unstable on Yahoo)
        return 0.0
    except Exception as e:
        print(f"❌ DXY error: {e}")
        return 0.0

def get_bitmex_lsr():
    try:
        # Static for now, replace with Coinglass webhook or API
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
        "news_sentiment": "neutral"  # placeholder
    }
