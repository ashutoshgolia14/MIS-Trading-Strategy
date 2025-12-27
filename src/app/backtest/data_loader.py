import csv
from datetime import datetime
from pathlib import Path

# Resolve project root robustly
BASE_DIR = Path(__file__).resolve().parents[2]

def load_csv(path):
    csv_path = BASE_DIR / path
    with open(csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {
                'ts': datetime.fromisoformat(row['timestamp']),
                'price': float(row['price'])
            }
