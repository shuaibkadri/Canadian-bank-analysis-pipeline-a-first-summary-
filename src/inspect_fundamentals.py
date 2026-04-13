import pandas as pd

df = pd.read_csv("data/processed/fundamentals_api.csv")

print("\n--- FUNDAMENTALS API DATA ---\n")
print(df)

print("\n--- INFO ---\n")
print(df.info())

print("\n--- MISSING VALUES ---\n")
print(df.isna().sum())

print("\n--- BASIC CHECKS ---\n")
print("Rows:", len(df))
print("Tickers:", df["ticker"].tolist())
print("\n--- FIXING MISSING TICKERS ---\n")

# fill missing ticker for National Bank
df.loc[df["bank"] == "National Bank", "ticker"] = "NA"

print(df)
df.to_csv("data/processed/fundamentals_clean.csv", index=False)

print("\nSaved cleaned fundamentals to data/processed/fundamentals_clean.csv")