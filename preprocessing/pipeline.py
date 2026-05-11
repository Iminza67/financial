import pandas as pd


def run_pipeline():

    # -----------------------------------
    # LOAD CLEAN DATASET
    # -----------------------------------
    df = pd.read_csv("data/crypto_data.csv")

    # -----------------------------------
    # CLEAN TYPES
    # -----------------------------------
    df["date"] = pd.to_datetime(df["date"])

    df["symbol"] = (
        df["symbol"]
        .astype("category")
    )

    float_cols = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "market_cap"
    ]

    for col in float_cols:
        df[col] = (
            pd.to_numeric(df[col], errors="coerce")
            .astype("float32")
        )

    # -----------------------------------
    # MOVING AVERAGES
    # -----------------------------------
    df["ma_7"] = (
        df.groupby("symbol")["close"]
        .transform(lambda x: x.rolling(7).mean())
    )

    df["ma_30"] = (
        df.groupby("symbol")["close"]
        .transform(lambda x: x.rolling(30).mean())
    )

    # -----------------------------------
    # RETURNS
    # -----------------------------------
    df["returns"] = (
        df.groupby("symbol")["close"]
        .pct_change() * 100
    )

    # -----------------------------------
    # REMOVE NaNs
    # -----------------------------------
    df = df.dropna()

    return df