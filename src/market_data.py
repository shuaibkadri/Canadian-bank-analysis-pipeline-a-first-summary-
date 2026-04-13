import yfinance as yf
import pandas as pd

tickers = ["RY.TO", "TD.TO", "BNS.TO", "BMO.TO", "CM.TO", "NA.TO"]

all_data = []

for ticker in tickers:
    try:
        data = yf.download(
            ticker,
            period="1y",
            auto_adjust=False,
            group_by="column",
            multi_level_index=False,
            progress=False,
        )

        print(f"\nColumns for {ticker}: {list(data.columns)}\n")

        close_prices = data["Adj Close"].rename(ticker)
        all_data.append(close_prices)

    except Exception as e:
        print(f"Failed for {ticker}: {e}")

df_prices = pd.concat(all_data, axis=1)

print("\n--- STOCK PRICE DATA ---\n")
print(df_prices.tail())
print("\n--- 1 YEAR RETURNS ---\n")

returns = ((df_prices.iloc[-1] / df_prices.iloc[0]) - 1) * 100
returns = returns.sort_values(ascending=False)

print(returns)
returns_df = returns.reset_index()
returns_df.columns = ["ticker", "return_1y_pct"]

print("\n--- RETURNS DATAFRAME ---\n")
print(returns_df)
returns_df["ticker"] = returns_df["ticker"].str.replace(".TO", "", regex=False)

print("\n--- CLEANED RETURNS DATAFRAME ---\n")
print(returns_df)
returns_df.to_csv("data/processed/market_returns.csv", index=False)

print("\nSaved market returns to data/processed/market_returns.csv")        
returns_df = returns.reset_index()
returns_df.columns = ["ticker", "return_1y_pct"]
returns_df["ticker"] = returns_df["ticker"].str.replace(".TO", "", regex=False)
returns_df.to_csv("data/processed/market_returns.csv", index=False)