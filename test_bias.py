# test_bias.py

from macro_bias_layer import score_macro_bias

if __name__ == "__main__":
    result = score_macro_bias()
    print("\n🧠 Macro Bias Report")
    print(f"Bias Score: {result['macro_bias']}")
    for r in result["reasons"]:
        print(f"→ {r}")
    print(f"Block Sniper: {result['block_sniper']}")
