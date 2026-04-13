import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load cleaned fundamentals
# -----------------------------
df = pd.read_csv("data/processed/fundamentals_clean.csv")

print("\n--- FUNDAMENTALS DATA ---\n")
print(df)

# -----------------------------
# Calculate core metrics
# -----------------------------
df["roe"] = df["net_income"] / df["total_equity"]
df["roe_pct"] = df["roe"] * 100

df["roa"] = df["net_income"] / df["total_assets"]
df["roa_pct"] = df["roa"] * 100

df["leverage"] = df["total_assets"] / df["total_equity"]

# Round for readability
df["roe_pct"] = df["roe_pct"].round(2)
df["roa_pct"] = df["roa_pct"].round(3)
df["leverage"] = df["leverage"].round(2)

# -----------------------------
# Create analysis table
# -----------------------------
analysis = df[
    ["bank", "ticker", "net_income", "roe_pct", "roa_pct", "leverage"]
].sort_values(by="roe_pct", ascending=False)

print("\n--- ANALYSIS TABLE ---\n")
print(analysis)

# Save analysis table
analysis.to_csv("data/processed/fundamentals_analysis.csv", index=False)

# -----------------------------
# Load market returns
# -----------------------------
returns_df = pd.read_csv("data/processed/market_returns.csv")

print("\n--- MARKET RETURNS ---\n")
print(returns_df)

# -----------------------------
# Merge fundamentals + returns
# -----------------------------
merged = pd.merge(
    analysis,
    returns_df,
    on="ticker",
    how="left"
)

print("\n--- MERGED FUNDAMENTALS + RETURNS ---\n")
print(merged)

# Save merged file
merged.to_csv("data/processed/final_merged_analysis.csv", index=False)

# -----------------------------
# Visualization
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(merged["roe_pct"], merged["return_1y_pct"])

for _, row in merged.iterrows():
    plt.text(row["roe_pct"], row["return_1y_pct"], row["bank"])

plt.xlabel("ROE (%)")
plt.ylabel("1-Year Return (%)")
plt.title("Canadian Banks: ROE vs Stock Returns")
plt.grid(True)
plt.tight_layout()

plt.savefig("outputs/charts/roe_vs_returns.png")
plt.show()

print("\nSaved chart to outputs/charts/roe_vs_returns.png")
print("Saved merged dataset to data/processed/final_merged_analysis.csv")