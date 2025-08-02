# macro_bias_layer.py

from macro_fetcher import get_macro_data

def score_macro_bias():
    data = get_macro_data()
    score = 0
    reasons = []

    # === DXY ===
    if data.get("dxy_change_1d", 0) > 0.5:
        score -= 1
        reasons.append("DXY rising → USD strength = risk-off")

    # === VIX ===
    if data.get("vix", 0) > 20:
        score -= 1
        reasons.append("VIX > 20 → volatility spike")

    # === US10Y ===
    if data.get("us10y", 0) > 4.0:
        score -= 1
        reasons.append("10Y yield > 4% → bonds attracting capital")

    # === BitMEX Long/Short Ratio ===
    if data.get("bitmex_lsr", 1.0) > 3.0:
        score -= 2
        reasons.append("BitMEX L/S > 3.0 → crowded longs")

    # === ETF/Fed News Sentiment (optional future hook) ===
    if data.get("news_sentiment") == "bearish":
        score -= 2
        reasons.append("Bearish macro news detected")

    block_sniper = score <= -2

    return {
        "macro_bias": score,
        "block_sniper": block_sniper,
        "reasons": reasons
    }
