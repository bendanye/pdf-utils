from typing import List

from PyPDF2 import PdfReader, PdfWriter

from page_range import PageRange
from page_single import PageSingle
from page_builder import PageBuilder


def extract_pdf(pdf_file_path: str, pages: List) -> str:
    page_builder = PageBuilder()
    for page in pages:
        if type(page) is PageSingle:
            page_builder.add_page_single(page.single_page)
        elif type(page) is PageRange:
            page_builder.add_page_range(page.from_page, page.to_page)

    return _extract(pdf_file_path, page_builder.build())


def _extract(pdf_file_path: str, pages: List[int]) -> None:
    pdf = PdfReader(pdf_file_path)
    pdf_writer = PdfWriter()

    for page_num in pages:
        pdf_writer.add_page(
            pdf.pages[page_num - 1]
        )  # page 1 in pdf.pages is 0 so must - 1

    file_base_name = pdf_file_path.replace(".pdf", "")
    output_file_name = f"{file_base_name}_extracted.pdf"
    with open(output_file_name, "wb") as f:
        pdf_writer.write(f)

    return output_file_name
