
import yfinance as yf
import pandas as pd

coins = {
    "BTC-USD": "Bitcoin",
    "ETH-USD": "Ethereum",
    "SOL-USD": "Solana",
    "XRP-USD": "XRP",
    "ADA-USD": "Cardano"
}

all_data = []

for ticker, name in coins.items():

    df = yf.download(
        ticker,
        start="2023-01-01",
        end="2026-01-01"
    )

    df.reset_index(inplace=True)

    df["symbol"] = ticker
    df["name"] = name

    all_data.append(df)

final_df = pd.concat(all_data)

final_df.to_csv("data/crypto_prices.csv", index=False)

print("Dataset saved.")