# 📈 Real-Time Quantitative Stock Analysis & Cloud Ingestion Pipeline

An end-to-end automated pipeline that fetches live 1-minute interval stock data, computes technical indicators (RSI, price deltas), and streams updates to a Power BI dashboard in near real-time via REST API. Deployed on PythonAnywhere for 24/7 cloud operation.

<img width="1407" height="769" alt="Screenshot 2026-03-28 064912" src="https://github.com/user-attachments/assets/6579c810-9872-4544-8cb4-8e0fb56f9708" />
<img width="1279" height="716" alt="Screenshot 2026-03-26 210531" src="https://github.com/user-attachments/assets/f27d3df6-29a8-414b-801b-6cbcfbd994b1" />


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
