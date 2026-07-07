# Interactive Tools Library

A collection of interactive tools built with Claude, for power-users.
Each tool is self-contained, immediately usable, and genuinely practical — not demo quality.

---

## Tools

| # | Tool | Use Case | Type |
|---|------|----------|------|
| 01 | [Learning Progress Tracker](01-learning-progress-tracker/) | Track completion of an 8-week × 5-class program visually | HTML Artifact |
| 02 | [Prompt Quality Checker](02-prompt-quality-checker/) | Score any prompt on Context, Task, and Format (1–10) | HTML Artifact |
| 03 | [Data Cleaner Script](03-data-cleaner-script/) | Clean messy CSVs: dedup, fill missing values, normalize columns | Python Script |

---

## How to use each tool

### 01 — Learning Progress Tracker
1. Open `01-learning-progress-tracker/learning-progress-tracker.html` in your browser.
2. Click cells in the grid or use the form to log completed classes.
3. Watch the progress bar and percentage update live.

### 02 — Prompt Quality Checker
1. Open `02-prompt-quality-checker/prompt-quality-checker.html` in your browser.
2. Paste any prompt in the text area and click **Score My Prompt**.
3. Read per-criterion scores and the improvement tips, then iterate.

### 03 — Data Cleaner Script
1. Make sure Python 3.9+ and pandas are installed (`pip install pandas`).
2. Run:
   ```bash
   python 03-data-cleaner-script/data-cleaner.py your_file.csv
   ```
3. A cleaned CSV and a summary report are produced automatically.

---

## Project structure

```
.
├── README.md                              ← you are here
├── TOOLS-INDEX.md                         ← quick reference index
├── plan.md                                ← build plan (meta)
├── todo.md                                ← original spec
│
├── 01-learning-progress-tracker/
│   ├── learning-progress-tracker.html
│   └── README.md
│
├── 02-prompt-quality-checker/
│   ├── prompt-quality-checker.html
│   └── README.md
│
└── 03-data-cleaner-script/
    ├── data-cleaner.py
    └── README.md
```
