import pandas as pd

def load_crypto_data():

    df = pd.read_csv(
        "data/crypto_prices.csv"
    )

    return df