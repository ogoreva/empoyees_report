from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_COLOR_INDEX


def exporter(items: list[dict]):
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    head = doc.add_paragraph('Отчет по загрузке')
    doc.add_paragraph()
    head.alignment = WD_ALIGN_PARAGRAPH.CENTER

    table = doc.add_table(1, 2, 'TableGrid')
    head_cells = table.rows[0].cells

    for i, item in enumerate(['Отдел', 'Количество задач']):
        p = head_cells[i].paragraphs[0]
        p.color = WD_COLOR_INDEX.GRAY_50
        p.add_run(item).bold = True
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for row in items:
        cells = table.add_row().cells
        p0 = cells[0].paragraphs[0]
        p0.text = f"Отдел {row['department']}"
        p0.runs[0].bold = True

        p1 = cells[1].paragraphs[0]
        p1.text = str(row['total_task'])
        p1.runs[0].bold = True
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER

        for i in sorted(row['employees'], key=lambda x: x["tasks"], reverse=True):
            cells = table.add_row().cells
            cells[0].text = str(i['name'])
            p2 = cells[1].paragraphs[0]
            p2.text = str(i['tasks'])
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.save('test.docx')
