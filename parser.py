import pandas as pd
from pathlib import Path


def parse(path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    employees = pd.read_excel(path, sheet_name="Сотрудники")
    tasks = pd.read_excel(path, sheet_name="Задачи")
    return employees, tasks
