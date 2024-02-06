from pathlib import Path

from loguru import logger

from exporter import docx_exporter
from handler import handler
from parser import parse


def main():
    logger.info("Startup process...")
    path = Path("Data.xlsb")
    if not path.exists():
        logger.error("Data for reporting is not found")
        logger.info("Stopping process...")
    logger.debug("Found file for processing")
    employees, tasks = parse(path)
    res = handler(employees, tasks)
    report_path = Path(__file__).parent / "report.docx"
    docx_exporter(res, report_path)
    assert report_path.exists(), "Something wrong during saving process"


if __name__ == '__main__':
    main()
