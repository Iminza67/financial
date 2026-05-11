import pandas as pd

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv(
    "data/crypto_prices.csv",
    header=[0, 1]
)

# -----------------------------
# BASIC INFO
# -----------------------------
print("\n====================")
print("DATAFRAME SHAPE")
print("====================")
print(df.shape)

print("\n====================")
print("COLUMN HEADERS")
print("====================")
print(df.columns)

print("\n====================")
print("FIRST 5 ROWS")
print("====================")
print(df.head())

print("\n====================")
print("DATA TYPES")
print("====================")
print(df.dtypes)

print("\n====================")
print("MISSING VALUES")
print("====================")
print(df.isnull().sum())

print("\n====================")
print("MEMORY USAGE")
print("====================")
print(df.memory_usage(deep=True))

print("\n====================")
print("SAMPLE BTC COLUMNS")
print("====================")

try:
    print(df[[
        ("Close", "BTC-USD"),
        ("Volume", "BTC-USD")
    ]].head())

except Exception as e:
    print("Error accessing BTC columns:")
    print(e)