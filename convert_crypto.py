import pandas as pd

# -----------------------------------
# LOAD RAW FILE
# -----------------------------------
df = pd.read_csv(
    "data/crypto_prices.csv",
    header=[0, 1]
)

# -----------------------------------
# FIX DATE COLUMN
# -----------------------------------
date_col = ("Date", "Unnamed: 0_level_1")

# -----------------------------------
# CRYPTOS
# -----------------------------------
cryptos = [
    "BTC-USD",
    "ETH-USD",
    "SOL-USD",
    "XRP-USD",
    "ADA-USD"
]

all_frames = []

# -----------------------------------
# PROCESS EACH CRYPTO
# -----------------------------------
for crypto in cryptos:

    temp = pd.DataFrame()

    temp["date"] = df[date_col]

    temp["close"] = df[("Close", crypto)]
    temp["high"] = df[("High", crypto)]
    temp["low"] = df[("Low", crypto)]
    temp["open"] = df[("Open", crypto)]
    temp["volume"] = df[("Volume", crypto)]

    # REMOVE EMPTY ROWS
    temp = temp.dropna()

    # SYMBOL
    temp["symbol"] = crypto.replace("-USD", "")

    # SIMPLE MARKET CAPS
    market_caps = {
        "BTC": 1800000000000,
        "ETH": 450000000000,
        "SOL": 70000000000,
        "XRP": 120000000000,
        "ADA": 35000000000
    }

    temp["market_cap"] = market_caps[
        crypto.replace("-USD", "")
    ]

    all_frames.append(temp)

# -----------------------------------
# MERGE EVERYTHING
# -----------------------------------
final_df = pd.concat(
    all_frames,
    ignore_index=True
)

# -----------------------------------
# CLEAN TYPES
# -----------------------------------
final_df["date"] = pd.to_datetime(final_df["date"])

float_cols = [
    "close",
    "high",
    "low",
    "open",
    "volume",
    "market_cap"
]

for col in float_cols:
    final_df[col] = (
        pd.to_numeric(final_df[col], errors="coerce")
        .astype("float32")
    )

final_df["symbol"] = (
    final_df["symbol"]
    .astype("category")
)

# -----------------------------------
# SORT
# -----------------------------------
final_df = final_df.sort_values(
    ["symbol", "date"]
)

# -----------------------------------
# SAVE CLEAN DATASET
# -----------------------------------
final_df.to_csv(
    "data/crypto_data.csv",
    index=False
)

print("\n====================")
print("FINAL DATASET CREATED")
print("====================")
print(final_df.head())

print("\nShape:")
print(final_df.shape)

print("\nMemory usage (MB):")
print(
    final_df.memory_usage(deep=True).sum()
    / 1024**2
)