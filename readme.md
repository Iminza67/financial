# Cryptocurrency Market Dashboard

A lightweight interactive cryptocurrency analytics dashboard built with Python, Dash, and Plotly.

The dashboard provides interactive visualizations for major cryptocurrencies including price trends, trading volume, returns, moving averages, and market capitalization insights.

---

# Live Demo

🚀 Deployed Application:

[https://financial-7jsz.onrender.com/](https://financial-7jsz.onrender.com/)

---

# Features

## 📈 Interactive Price Charts

* Candlestick charts
* Historical closing price visualization
* Interactive hover tooltips

## 📊 Trading Volume Analysis

* Volume trend charts
* Market activity visualization

## 📉 Returns Analysis

* Daily returns visualization
* Price performance tracking

## 📌 Moving Averages

* Short-term moving averages
* Long-term moving averages
* Trend analysis support

## 🌙 Dark Mode Interface

* Modern dark-themed dashboard
* Improved readability and visual experience

## 🪙 Supported Cryptocurrencies

* Bitcoin (BTC)
* Ethereum (ETH)
* Solana (SOL)
* XRP
* Cardano (ADA)

## 💰 Market Capitalization Information

* Market cap metrics integrated into the dashboard

## 🖼 Cryptocurrency Logos

* Visual branding support for cryptocurrencies

---

# Technologies Used

* Python
* Dash
* Plotly
* Pandas
* NumPy
* Gunicorn
* Render

---

# Project Structure

```bash
project/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── data/
│   └── crypto_clean.csv
│
├── visuals/
│   ├── candlestick.py
│   ├── moving_average.py
│   ├── returns_chart.py
│   ├── volume.py
│   └── marketcap.py
│
└── assets/
    └── styles.css
```

---

# Dataset

The dataset contains historical cryptocurrency market data including:

* Open price
* High price
* Low price
* Close price
* Trading volume
* Market capitalization

The data was cleaned and transformed into a dashboard-ready format using Pandas preprocessing pipelines.

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/crypto-dashboard.git
cd crypto-dashboard
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

---

# Activate Virtual Environment

## Windows

```bash
venv\Scripts\activate
```

## Mac/Linux

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application Locally

```bash
python app.py
```

The dashboard will run on:

```bash
http://127.0.0.1:8050/
```

---

# Deployment

The application is deployed on Render using:

* Gunicorn
* Python runtime
* Render Web Service hosting

---

# Performance Optimization

The project was optimized for lightweight deployment by:

* Preprocessing datasets before deployment
* Reducing runtime calculations
* Cleaning missing and invalid data
* Simplifying heavy visualizations
* Reducing overall memory usage

---

# Future Improvements

* Real-time cryptocurrency API integration
* Portfolio tracking functionality
* Additional cryptocurrencies
* Advanced technical indicators
* Predictive analytics
* User authentication system

---

# Author

Olivia Iminza Hamisi

Bachelor of Science in Engineering (Informatics)
IMC University of Applied Sciences Krems

---

# License

This project is for educational and portfolio purposes.
