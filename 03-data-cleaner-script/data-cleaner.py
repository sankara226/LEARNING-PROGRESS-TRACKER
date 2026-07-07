"""
data-cleaner.py
---------------
Cleans a messy CSV file and outputs a cleaned version.

Operations performed:
  - Standardize column names (lowercase, spaces → underscores)
  - Remove duplicate rows
  - Handle missing values (fill with 'unknown' for object columns,
    0 for numeric columns — see --drop-missing flag to drop instead)
  - Print a summary: rows before/after, columns, data types

Usage:
  python data-cleaner.py input.csv
  python data-cleaner.py input.csv --output cleaned.csv
  python data-cleaner.py input.csv --drop-missing
"""

import argparse
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Error: pandas is required. Install it with:  pip install pandas")
    sys.exit(1)


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase column names and replace spaces/special chars with underscores."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return df


def remove_duplicates(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Drop fully duplicate rows and return (cleaned_df, count_removed)."""
    before = len(df)
    df = df.drop_duplicates()
    return df, before - len(df)


def handle_missing(df: pd.DataFrame, drop: bool = False) -> tuple[pd.DataFrame, dict]:
    """
    Fill or drop missing values.
    Returns (cleaned_df, dict of {column: missing_count}).
    """
    missing_counts = df.isnull().sum()
    missing_report = {
        col: int(count)
        for col, count in missing_counts.items()
        if count > 0
    }

    if drop:
        df = df.dropna()
    else:
        for col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].fillna("unknown")
            else:
                df[col] = df[col].fillna(0)

    return df, missing_report


def print_summary(
    original_rows: int,
    cleaned_rows: int,
    dupes_removed: int,
    missing_report: dict,
    df: pd.DataFrame,
    output_path: str,
) -> None:
    """Print a human-readable cleaning summary."""
    sep = "-" * 50

    print(f"\n{sep}")
    print("  DATA CLEANING SUMMARY")
    print(sep)

    print(f"\n  Rows")
    print(f"    Before : {original_rows:,}")
    print(f"    After  : {cleaned_rows:,}")
    print(f"    Removed: {original_rows - cleaned_rows:,}  "
          f"(dupes: {dupes_removed}, missing-row drops: "
          f"{original_rows - cleaned_rows - dupes_removed})")

    print(f"\n  Columns ({len(df.columns)} total)")
    for col in df.columns:
        dtype = str(df[col].dtype)
        missing_note = f"  <- had {missing_report[col]} missing" if col in missing_report else ""
        print(f"    {col:<30} {dtype}{missing_note}")

    if missing_report:
        print(f"\n  Missing values handled")
        for col, count in missing_report.items():
            print(f"    {col}: {count} cell(s)")

    print(f"\n  Output saved to: {output_path}")
    print(f"{sep}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Clean a messy CSV file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", help="Path to the input CSV file")
    parser.add_argument(
        "--output", "-o",
        help="Path for the cleaned CSV (default: <input>_cleaned.csv)",
        default=None,
    )
    parser.add_argument(
        "--drop-missing",
        action="store_true",
        help="Drop rows with missing values instead of filling them",
    )
    args = parser.parse_args()

    # Resolve paths
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: file not found — {input_path}")
        sys.exit(1)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_stem(input_path.stem + "_cleaned")

    # Load
    try:
        df = pd.read_csv(input_path)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    original_rows = len(df)
    print(f"Loaded {original_rows:,} rows x {len(df.columns)} columns from '{input_path.name}'")

    # Clean
    df = standardize_columns(df)
    df, dupes_removed = remove_duplicates(df)
    df, missing_report = handle_missing(df, drop=args.drop_missing)

    # Save
    df.to_csv(output_path, index=False)

    # Report
    print_summary(
        original_rows=original_rows,
        cleaned_rows=len(df),
        dupes_removed=dupes_removed,
        missing_report=missing_report,
        df=df,
        output_path=str(output_path),
    )


if __name__ == "__main__":
    main()
