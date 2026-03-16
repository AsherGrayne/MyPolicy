import os

import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS1_DIR = os.path.join(
    BASE_DIR,
    "data-pipeline-service",
    "datasets1",
)


def convert_all_csv_to_xlsx() -> None:
    for name in os.listdir(DATASETS1_DIR):
        if not name.lower().endswith(".csv"):
            continue
        csv_path = os.path.join(DATASETS1_DIR, name)
        xlsx_path = csv_path[:-4] + ".xlsx"

        print(f"Converting {csv_path} -> {xlsx_path}")
        df = pd.read_csv(csv_path)
        df.to_excel(xlsx_path, index=False)


if __name__ == "__main__":
    convert_all_csv_to_xlsx()

