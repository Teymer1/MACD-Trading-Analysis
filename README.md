# 📈 Stock Trading Strategy Analysis (MACD)

A Python-based financial analysis tool that implements the **MACD (Moving Average Convergence Divergence)** strategy to identify buy and sell signals for example stock.

## ⚠️ Disclaimer
This project is for **educational and research purposes only**. The trading strategy and analysis provided are not financial advice. Past performance of the MACD indicator does not guarantee future results. **Use this code at your own risk**; never trade with money you cannot afford to lose.
## 🚀 Overview
This project simulates a trading strategy based on technical indicators. It processes historical stock data from 2021 to 2025, calculates EMA-based indicators, and visualizes the performance of an investment portfolio.

## 🛠️ Features
* **Technical Indicators**: Custom implementation of EMA, MACD Line, and Signal Line.
* **Backtesting Engine**: Simulates trading based on crossovers to calculate final portfolio value.
* **Detailed Analytics**: Generates a trade log including profit/loss per transaction and strategy efficiency.
* **Advanced Visualization**: Interactive plots showing price action, indicators, and trade entry/exit points.

## 📂 Project Structure
* `data_loader.py`: Handles CSV parsing and date-based filtering.
* `indicators.py`: Pure mathematical logic for EMA and MACD.
* `trading_engine.py`: Signal detection and portfolio simulation.
* `visualization.py`: Matplotlib wrappers for financial charting.
* `main.py`: The entry point to run the full analysis pipeline.

## 📊 Strategy Visualization
The model identifies trends by observing the relationship between the MACD Line and the Signal Line.



## 📈 Performance Summary
The strategy provides a clear view of:
* Total number of trades executed.
* Success rate (profitable vs. losing trades).
* Final capital vs. initial investment.

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Teymer1/MACD-Trading-Analysis.git
