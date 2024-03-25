import glob

from pypdf import PdfMerger
from natsort import natsorted


def merge(directory: str, merged_file_name: str = "merged.pdf") -> None:
    pdfs = natsorted(glob.glob(f"{directory}/*.pdf"))

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(merged_file_name)
    merger.close()


def main():
    merge(directory="")
