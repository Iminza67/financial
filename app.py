from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
from functools import lru_cache

from preprocessing.pipeline import run_pipeline

# -----------------------------
# LOAD DATA ONCE
# -----------------------------
@lru_cache
def get_data():
    return run_pipeline()

df = get_data()

symbols = sorted(df["symbol"].unique())

# -----------------------------
# LOGOS
# -----------------------------
crypto_logos = {
    "BTC": "https://cryptologos.cc/logos/bitcoin-btc-logo.png",
    "ETH": "https://cryptologos.cc/logos/ethereum-eth-logo.png",
    "SOL": "https://cryptologos.cc/logos/solana-sol-logo.png",
    "ADA": "https://cryptologos.cc/logos/cardano-ada-logo.png",
    "XRP": "https://cryptologos.cc/logos/xrp-xrp-logo.png"
}

# -----------------------------
# DASH APP
# -----------------------------
app = Dash(__name__)

app.layout = html.Div(

    style={
        "backgroundColor": "#111111",
        "color": "white",
        "minHeight": "100vh",
        "padding": "20px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Cryptocurrency Analytics Dashboard",
            style={
                "textAlign": "center",
                "marginBottom": "30px"
            }
        ),

        # -----------------------------
        # DROPDOWN
        # -----------------------------
        dcc.Dropdown(
            id="crypto-dropdown",
            options=[
                {"label": s, "value": s}
                for s in symbols
            ],
            value=symbols[0],
            style={
                "color": "black",
                "marginBottom": "20px"
            }
        ),

        # -----------------------------
        # LOGO + MARKET CAP
        # -----------------------------
        html.Div(
            id="crypto-info",
            style={
                "display": "flex",
                "alignItems": "center",
                "gap": "20px",
                "marginBottom": "20px"
            }
        ),

        # -----------------------------
        # PRICE + MOVING AVERAGES
        # -----------------------------
        dcc.Graph(id="price-chart"),

        # -----------------------------
        # CANDLESTICK
        # -----------------------------
        dcc.Graph(id="candlestick-chart"),

        # -----------------------------
        # VOLUME
        # -----------------------------
        dcc.Graph(id="volume-chart"),

        # -----------------------------
        # RETURNS
        # -----------------------------
        dcc.Graph(id="returns-chart")
    ]
)

# ------------------------------------------------
# INFO CARD
# ------------------------------------------------
@app.callback(
    Output("crypto-info", "children"),
    Input("crypto-dropdown", "value")
)
def update_info(symbol):

    filtered = df[df["symbol"] == symbol]

    latest_market_cap = (
        filtered["market_cap"]
        .dropna()
        .iloc[-1]
    )

    logo = crypto_logos.get(symbol)

    return [

        html.Img(
            src=logo,
            style={
                "height": "60px"
            }
        ),

        html.Div([
            html.H2(symbol),

            html.H4(
                f"Market Cap: ${latest_market_cap:,.0f}"
            )
        ])
    ]


# ------------------------------------------------
# PRICE + MOVING AVERAGES
# ------------------------------------------------
@app.callback(
    Output("price-chart", "figure"),
    Input("crypto-dropdown", "value")
)
def update_price_chart(symbol):

    filtered = df[df["symbol"] == symbol]

    fig = go.Figure()

    # PRICE
    fig.add_trace(go.Scatter(
        x=filtered["date"],
        y=filtered["close"],
        mode="lines",
        name="Close Price"
    ))

    # 7 DAY MA
    fig.add_trace(go.Scatter(
        x=filtered["date"],
        y=filtered["ma_7"],
        mode="lines",
        name="7-Day MA"
    ))

    # 30 DAY MA
    fig.add_trace(go.Scatter(
        x=filtered["date"],
        y=filtered["ma_30"],
        mode="lines",
        name="30-Day MA"
    ))

    fig.update_layout(
        title=f"{symbol} Price + Moving Averages",
        template="plotly_dark",
        height=500
    )

    return fig


# ------------------------------------------------
# CANDLESTICK
# ------------------------------------------------
@app.callback(
    Output("candlestick-chart", "figure"),
    Input("crypto-dropdown", "value")
)
def update_candlestick(symbol):

    filtered = df[df["symbol"] == symbol]

    fig = go.Figure(data=[go.Candlestick(
        x=filtered["date"],
        open=filtered["open"],
        high=filtered["high"],
        low=filtered["low"],
        close=filtered["close"]
    )])

    fig.update_layout(
        title=f"{symbol} Candlestick Chart",
        template="plotly_dark",
        height=600
    )

    return fig


# ------------------------------------------------
# VOLUME
# ------------------------------------------------
@app.callback(
    Output("volume-chart", "figure"),
    Input("crypto-dropdown", "value")
)
def update_volume(symbol):

    filtered = df[df["symbol"] == symbol]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=filtered["date"],
        y=filtered["volume"],
        name="Volume"
    ))

    fig.update_layout(
        title=f"{symbol} Trading Volume",
        template="plotly_dark",
        height=400
    )

    return fig


# ------------------------------------------------
# RETURNS
# ------------------------------------------------
@app.callback(
    Output("returns-chart", "figure"),
    Input("crypto-dropdown", "value")
)
def update_returns(symbol):

    filtered = df[df["symbol"] == symbol]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=filtered["date"],
        y=filtered["returns"],
        mode="lines",
        name="Returns (%)"
    ))

    fig.update_layout(
        title=f"{symbol} Daily Returns",
        template="plotly_dark",
        height=400
    )

    return fig


# ------------------------------------------------
# SERVER
# ------------------------------------------------
server = app.server

if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=8050
    )