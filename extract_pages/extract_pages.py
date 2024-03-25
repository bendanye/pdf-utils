from typing import List

from PyPDF2 import PdfReader, PdfWriter

from page_builder import PageBuilder


def extract(pdf_file_path: str, pages: List[int]) -> None:
    file_base_name = pdf_file_path.replace(".pdf", "")

    pdf = PdfReader(pdf_file_path)
    pdf_writer = PdfWriter()

    for page_num in pages:
        pdf_writer.add_page(
            pdf.pages[page_num - 1]
        )  # page 1 in pdf.pages is 0 so must - 1

    with open(f"{file_base_name}_extracted.pdf", "wb") as f:
        pdf_writer.write(f)


if __name__ == "__main__":
    page_builder = PageBuilder()

    # Examples
    pdf_file_path = "AWS Certified Cloud Practitioner Slides v10.pdf"
    pages = (
        page_builder.add_page(56)
        .add_page(91)
        .add_page(111)
        .add_page_range(220, 250)
        .build()
    )

    extract(pdf_file_path, pages)
