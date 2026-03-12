# Random Dataset Generator for Testing

## Description
Generates realistic fake datasets (users, sales, logs, sensor data) as CSV or JSON for development and testing.

## Features
- 4 dataset types: users, sales, logs, sensor
- Configurable row count
- Reproducible with seed
- CSV and JSON output
- Terminal preview

## Tech Stack
- Python 3.10+, pandas, numpy

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python main.py users -n 500 -o users.csv
python main.py sales -n 1000 -o sales.json
python main.py sensor -n 2880
```

## Example Output
```
📊 Generating 100 rows of 'users' data...
Preview (5 rows):
 id first_name last_name                       email  age country
  1      Alice     Smith    alice.smith@gmail.com   34      US
✅ Saved 100 rows to 'dataset.csv'
```
