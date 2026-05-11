from data.loaders import load_crypto_data

def run_pipeline():

    df = load_crypto_data()

    # Reduce memory
    df["symbol"] = df["symbol"].astype("category")

    return df