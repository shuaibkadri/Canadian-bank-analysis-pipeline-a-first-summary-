# Canadian Bank Fundamental Analysis Pipeline — Summary

## Project Objective
This project builds a small financial analysis pipeline for major Canadian banks by combining:
- real fundamental data from Yahoo Finance
- real market price data
- derived financial metrics
- visualization and interpretation

The goal is to compare Canadian banks on profitability and market performance, and test whether stronger fundamentals are associated with stronger stock returns.

## Banks Covered
- RBC
- TD
- Scotiabank
- BMO
- CIBC
- National Bank

## Data Sources
- Yahoo Finance fundamentals via `yfinance`
- Yahoo Finance historical stock prices via `yfinance`

## Methodology
The project follows four stages:

1. **Fundamentals ingestion**
   - Pull net income, total assets, and total equity for each bank
   - Save raw API output

2. **Data cleaning**
   - Inspect missing values
   - Correct ticker inconsistencies
   - Save cleaned fundamentals dataset

3. **Market data ingestion**
   - Download 1-year stock prices
   - Calculate 1-year returns
   - Save returns dataset

4. **Analysis**
   - Compute:
     - ROE
     - ROA
     - Leverage
   - Merge fundamentals with market returns
   - Visualize ROE against 1-year stock return

## Key Metrics
- **ROE (%)** = Net Income / Total Equity
- **ROA (%)** = Net Income / Total Assets
- **Leverage** = Total Assets / Total Equity
- **1-Year Return (%)** = (Latest Price / First Price - 1) × 100

## Main Insight
The analysis suggests a weak positive relationship between ROE and stock returns. Profitability appears relevant, but market performance is not explained by ROE alone. This implies that stock returns are influenced by additional factors such as expectations, risk perception, and broader market conditions.

## Interpretation Notes
- High ROE does not automatically lead to the highest stock return
- Large, mature banks may show strong profitability but more moderate market performance
- Smaller banks may show stronger returns relative to fundamentals if the market is pricing future growth more aggressively

## Outputs
This project produces:
- cleaned fundamentals dataset
- market returns dataset
- merged analysis dataset
- ROE vs Return chart

## Limitations
- Small sample size (6 banks)
- Single-period comparison
- Limited set of accounting variables
- Reliance on Yahoo Finance field availability and naming consistency

## Next Steps
Potential improvements:
- add valuation metrics such as P/B and dividend yield
- extend to multiple years of fundamentals
- include quarterly data
- build a dashboard
- compare Canadian banks with U.S. peers