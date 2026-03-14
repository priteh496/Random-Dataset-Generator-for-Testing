"""
Dataset generation logic using numpy and pandas.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from src.config import DATASET_TYPES


class DatasetGenerator:
    def __init__(self, seed: int = 42):
        self.rng = np.random.default_rng(seed)

    def generate(self, dataset_type: str, n: int) -> pd.DataFrame:
        method = getattr(self, f"_gen_{dataset_type}", None)
        if not method:
            raise ValueError(f"Unknown type: {dataset_type}")
        return method(n)

    def _rand_dates(self, n, start="2020-01-01", end="2024-12-31"):
        start_dt = datetime.strptime(start, "%Y-%m-%d")
        end_dt = datetime.strptime(end, "%Y-%m-%d")
        delta = (end_dt - start_dt).days
        offsets = self.rng.integers(0, delta, n)
        return [start_dt + timedelta(days=int(d)) for d in offsets]

    def _gen_users(self, n: int) -> pd.DataFrame:
        first = ["Alice","Bob","Carlos","Diana","Eve","Frank","Grace","Hank","Ivy","Jack"]
        last  = ["Smith","Jones","Williams","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson"]
        domains = ["gmail.com","yahoo.com","outlook.com","company.io"]
        f = [first[i % len(first)] for i in range(n)]
        l = [last[i % len(last)] for i in range(n)]
        return pd.DataFrame({
            "id": range(1, n+1),
            "first_name": f,
            "last_name": l,
            "email": [f"{a.lower()}.{b.lower()}@{domains[i%4]}" for i,(a,b) in enumerate(zip(f,l))],
            "age": self.rng.integers(18, 75, n),
            "country": self.rng.choice(["US","UK","DE","FR","CA","AU","JP","IN"], n),
            "signup_date": self._rand_dates(n),
            "is_active": self.rng.choice([True, False], n, p=[0.85, 0.15]),
        })

    def _gen_sales(self, n: int) -> pd.DataFrame:
        products = ["Widget A","Widget B","Gadget X","Gadget Y","Service Pro","Service Lite"]
        return pd.DataFrame({
            "order_id": [f"ORD-{1000+i}" for i in range(n)],
            "date": self._rand_dates(n),
            "product": self.rng.choice(products, n),
            "quantity": self.rng.integers(1, 20, n),
            "unit_price": np.round(self.rng.uniform(5.0, 500.0, n), 2),
            "discount": np.round(self.rng.uniform(0, 0.3, n), 2),
            "region": self.rng.choice(["North","South","East","West"], n),
            "rep_id": self.rng.integers(101, 120, n),
        })

    def _gen_logs(self, n: int) -> pd.DataFrame:
        levels = ["INFO","WARNING","ERROR","DEBUG"]
        services = ["auth","api","database","cache","worker"]
        messages = ["Request processed","Connection timeout","Invalid token","Cache miss","Job queued"]
        return pd.DataFrame({
            "timestamp": self._rand_dates(n, "2024-01-01", "2024-12-31"),
            "level": self.rng.choice(levels, n, p=[0.6, 0.2, 0.1, 0.1]),
            "service": self.rng.choice(services, n),
            "message": self.rng.choice(messages, n),
            "duration_ms": self.rng.integers(1, 2000, n),
            "status_code": self.rng.choice([200, 201, 400, 401, 404, 500], n, p=[0.6,0.1,0.1,0.05,0.1,0.05]),
        })

    def _gen_sensor(self, n: int) -> pd.DataFrame:
        t = pd.date_range("2024-01-01", periods=n, freq="1min")
        return pd.DataFrame({
            "timestamp": t,
            "temperature_c": np.round(20 + self.rng.normal(0, 3, n), 2),
            "humidity_pct": np.round(self.rng.uniform(30, 90, n), 1),
            "pressure_hpa": np.round(1013 + self.rng.normal(0, 5, n), 1),
            "co2_ppm": self.rng.integers(400, 2000, n),
            "device_id": [f"SENSOR-{self.rng.integers(1,5)}" for _ in range(n)],
        })
