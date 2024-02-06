import pandas as pd


def handler(employees: pd.DataFrame, tasks: pd.DataFrame) -> list[dict]:
    df = employees.set_index("Табельный номер").join(
        other=tasks.set_index("Табельный номер"),
        how="inner",
        lsuffix="_l",
        rsuffix="_r")
    df.fillna(value=" ", inplace=True)
    df['ФИО'] = df['Фамилия'].str.strip() + " " + df['Имя '].str[0] + "." + df['Отчество'].str[0] + "."
    df = df.drop(["Дата рождения", "Фамилия", "Имя ", "Отчество"], axis=1)
    df = df.groupby(["ФИО", "Отдел"]).count()
    df.reset_index(inplace=True)
    departments = df["Отдел"].unique()
    res = []
    for dep in departments:
        current = df[df["Отдел"] == dep]
        total_task = current["ИД\nзадачи"].sum()

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
        res.append(storage)
    res.sort(key=lambda x: x["total_task"], reverse=True)
    return res
