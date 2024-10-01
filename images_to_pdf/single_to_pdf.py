import glob
from typing import List

from PIL import Image
from natsort import natsorted


def to_pdf(directory: str) -> None:
    image_files = _get_images(directory)

    for image_path in image_files:
        image = Image.open(image_path).convert("RGB")
        pdf_path = f"{image_path}.pdf"
        image.save(pdf_path, "PDF", resolution=100.0)


def _get_images(directory: str) -> List[str]:
    result = []
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif", "*.tiff"):
        result.extend(natsorted(glob.glob(f"{directory}/{ext}")))

    return result


if __name__ == "__main__":
    to_pdf(directory="examples/alternate_between/questions")
