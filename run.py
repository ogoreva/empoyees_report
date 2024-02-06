from pathlib import Path
from parser import parse
from handler import handler
from exporter import exporter


def main():
    path = Path("Data.xlsb")
    employees, tasks = parse(path)
    res = handler(employees, tasks)
    exporter(res)


if __name__ == '__main__':
    main()

