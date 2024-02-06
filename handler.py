import pandas as pd


def handler(employees: pd.DataFrame, tasks: pd.DataFrame) -> list[dict]:
    """
    Prepare input data for the report
    :param employees:
    :param tasks:
    :return:
    """
    # Join tables by employee_id
    df = employees.set_index("Табельный номер").join(
        other=tasks.set_index("Табельный номер"),
        how="inner",
        lsuffix="_l",
        rsuffix="_r")
    # Fill missed data as " "
    df.fillna(value=" ", inplace=True)
    # Create new column with new name of employee
    df['ФИО'] = df['Фамилия'].str.strip() + " " + df['Имя '].str[0] + "." + df['Отчество'].str[0] + "."
    # Remove redundant columns
    df = df.drop(["Дата рождения", "Фамилия", "Имя ", "Отчество"], axis=1)
    # Aggregate employees
    df = df.groupby(["ФИО", "Отдел"]).count()
    # Remove index from table
    df.reset_index(inplace=True)
    # Get unique departments
    departments = df["Отдел"].unique()
    # Here will be a result
    res = []
    for dep in departments:
        # Filter df by particular department
        current = df[df["Отдел"] == dep]
        # Sum task by hole department
        total_task = current["ИД\nзадачи"].sum()
        # Create structure for further processing
        storage = {
            "department": dep,
            "total_task": total_task,
            "employees": [
                {
                    "name": record[1]["ФИО"],
                    "tasks": record[1]["ИД\nзадачи"]
                } for record in current.iterrows()
            ]
        }
        # Append it to result
        res.append(storage)
    # sort `storage` object by total_task in descending order
    res.sort(key=lambda x: x["total_task"], reverse=True)
    return res
