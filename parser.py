from pathlib import Path

import pandas as pd
from loguru import logger


def parse(path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Read excel file and return pandas DataFrame
    :param path: path to excel file
    :return: DataFrame
    """
    # Read input data here by sheet name and return it
    logger.debug("Start parsing process")
    employees = pd.read_excel(path, sheet_name="Сотрудники")
    logger.debug(f"Employees table contain {employees.shape[0]} rows")
    tasks = pd.read_excel(path, sheet_name="Задачи")
    logger.debug(f"Tasks table contain {tasks.shape[0]} rows")
    return employees, tasks
