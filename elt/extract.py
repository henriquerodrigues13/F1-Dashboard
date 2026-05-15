from config import RAW_DIR
from pathlib import Path
import pandas as pd


def load_dataframe() -> dict[str, pd.DataFrame]:
    files = [
        "circuits",
        "constructor_standings",
        "constructors",
        "driver_standings",
        "drivers",
        "qualifying",
        "races",
        "results",
    ]

    return {
        f"{name}": pd.read_csv(Path(RAW_DIR) / f"f1_{name}.csv")
        for name in files
    }

