from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

from preprocessing.pipeline import run_pipeline

df = run_pipeline()

symbols = df["symbol"].unique()

app = Dash(__name__)

app.layout = html.Div([

    html.H1("Crypto Dashboard"),

    dcc.Dropdown(
        id="crypto-dropdown",
        options=[
            {"label": s, "value": s}
            for s in symbols
        ],
        value=symbols[0]
    ),

    dcc.Graph(id="candlestick"),

    dcc.Graph(id="volume")

])

@app.callback(
    Output("candlestick", "figure"),
    Input("crypto-dropdown", "value")
)
def update_chart(symbol):

    filtered = df[df["symbol"] == symbol]

    fig = go.Figure(data=[
        go.Candlestick(
            x=filtered["Date"],
            open=filtered["Open"],
            high=filtered["High"],
            low=filtered["Low"],
            close=filtered["Close"]
        )
    ])

    return fig


@app.callback(
    Output("volume", "figure"),
    Input("crypto-dropdown", "value")
)
def update_volume(symbol):

    filtered = df[df["symbol"] == symbol]

    fig = go.Figure()

    fig.add_bar(
        x=filtered["Date"],
        y=filtered["Volume"]
    )

    return fig


server = app.server

if __name__ == "__main__":
    app.run_server(debug=False)