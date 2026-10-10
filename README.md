# 📈 Real-Time Quantitative Stock Analysis & Cloud Ingestion Pipeline

An end-to-end automated pipeline that fetches live 1-minute interval stock data, computes technical indicators (RSI, price deltas), and streams updates to a Power BI dashboard in near real-time via REST API. Deployed on PythonAnywhere for 24/7 cloud operation.

![Dashboard Preview](https://i.imgur.com/your-dashboard-screenshot.png)  
*(Replace with an actual screenshot from your Power BI dashboard)*

## 🚀 Features

- **Real-Time Data Extraction**: Fetches 1-minute OHLCV data for blue-chip equities (AAPL, AMD, GOOGL, MSFT, NVDA, TSLA) using `yfinance`.
- **Technical Indicators**: Calculates 14-period RSI, intraday price deltas, and generates Overbought (>70) / Oversold (<30) signals.
- **Cloud Orchestration**: Runs continuously on PythonAnywhere with custom proxy and market-hour scheduling.
- **Live Power BI Integration**: Pushes JSON payloads every 15 seconds to a Power BI Streaming Dataset via REST API.
- **Interactive Dashboard**: Displays live price trends, volume, RSI, signal variations, and summary tables.

## 🏗️ Architecture
┌─────────────────┐ ┌──────────────────┐ ┌────────────────────┐
│ Yahoo Finance │────▶│ Python Engine │────▶│ Power BI Streaming│
│ (yfinance API) │ │ (PythonAnywhere)│ │ Dataset (REST API)│
└─────────────────┘ └──────────────────┘ └────────────────────┘
│
▼
┌──────────────┐
│ Feature │
│ Engineering │
│ (RSI, etc.) │
└──────────────┘

## 🛠️ Technologies Used

- **Python 3.10+**
- **yfinance** – market data
- **pandas / numpy** – data manipulation
- **requests** – REST API calls
- **PythonAnywhere** – cloud hosting
- **Power BI** – streaming dashboard

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sri-Mathi-A/Real-time-Stock-Dashboard.git
   cd Real-time-Stock-Dashboard