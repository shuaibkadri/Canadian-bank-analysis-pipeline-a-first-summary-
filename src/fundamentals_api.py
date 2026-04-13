import yfinance as yf
import pandas as pd
tickers = {
    "RBC": "RY.TO",
    "TD": "TD.TO",
    "Scotiabank": "BNS.TO",
    "BMO": "BMO.TO",
    "CIBC": "CM.TO",
    "National Bank": "NA.TO"
}
rows = []

for bank_name, ticker in tickers.items():
    print(f"\nProcessing {bank_name} ({ticker})...")

    try:
        stock = yf.Ticker(ticker)

        income_stmt = stock.financials
        balance_sheet = stock.balance_sheet

        print("Income statement rows:")
        print(income_stmt.index.tolist()[:10])

        print("Balance sheet rows:")
        print(balance_sheet.index.tolist()[:10])

        net_income = income_stmt.loc["Net Income"].iloc[0]
        total_assets = balance_sheet.loc["Total Assets"].iloc[0]
        total_equity = balance_sheet.loc["Stockholders Equity"].iloc[0]

        rows.append({
            "bank": bank_name,
            "ticker": ticker.replace(".TO", ""),
            "net_income": net_income,
            "total_assets": total_assets,
            "total_equity": total_equity
        })
    except Exception as e:
        print(f"Failed for {bank_name}: {e}")
df = pd.DataFrame(rows)

print("\n--- FUNDAMENTALS DATAFRAME ---\n")
print(df)

df.to_csv("data/processed/fundamentals_api.csv", index=False)
print("\nSaved to data/processed/fundamentals_api.csv")