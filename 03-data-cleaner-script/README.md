# 03 — Data Cleaner Script

**Type:** Python script
**File:** `data-cleaner.py`

## What it does

Takes a messy CSV file and outputs a cleaned version. Useful for preprocessing raw exports from spreadsheets, form submissions, or scraped data before analysis.

**Operations:**
1. **Standardize column names** — lowercase, spaces and special characters replaced with underscores
2. **Remove duplicate rows** — fully identical rows are dropped
3. **Handle missing values** — fills `object` columns with `"unknown"`, numeric columns with `0` (or drops rows with `--drop-missing`)
4. **Print a summary** — rows before/after, columns with data types, missing value counts

## Requirements

- Python 3.9+
- pandas

Install pandas if needed:

```bash
pip install pandas
```

## Usage

```bash
# Basic — output saved as input_cleaned.csv
python data-cleaner.py my_data.csv

# Specify output file
python data-cleaner.py my_data.csv --output clean/result.csv

# Drop rows with missing values instead of filling them
python data-cleaner.py my_data.csv --drop-missing
```

## Example output

```
Loaded 1,500 rows × 6 columns from 'sales_export.csv'

──────────────────────────────────────────────────
  DATA CLEANING SUMMARY
──────────────────────────────────────────────────

  Rows
    Before : 1,500
    After  : 1,431
    Removed: 69  (dupes: 12, missing-row drops: 0)

  Columns (6 total)
    customer_id                    int64
    full_name                      object  ← had 3 missing
    email                          object  ← had 8 missing
    purchase_date                  object
    amount_usd                     float64 ← had 14 missing
    region                         object  ← had 22 missing

  Missing values handled
    full_name: 3 cell(s)
    email: 8 cell(s)
    amount_usd: 14 cell(s)
    region: 22 cell(s)

  Output saved to: sales_export_cleaned.csv
──────────────────────────────────────────────────
```
