from typing import List

from extract_pages import extract_pdf

from page_range import PageRange
from page_single import PageSingle


if __name__ == "__main__":
    # for example
    pdf_file_path = "test.pdf"
    pages = []
    pages.append(PageSingle(single_page=56))
    pages.append(PageSingle(single_page=91))
    pages.append(PageSingle(single_page=111))
    pages.append(PageRange(from_page=220, to_page=250))

    extract_pdf(pdf_file_path, pages)
