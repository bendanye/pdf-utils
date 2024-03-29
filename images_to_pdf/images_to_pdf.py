import glob
from typing import List

from PIL import Image, ImageDraw
from natsort import natsorted


def to_pdf(title: str, directories: List[str], image_order: str = "sequential") -> None:
    if image_order == "sequential":
        image_files = _sequential(directories)
    elif image_order == "alternate_between":
        image_files = _alternate_between(directories)
    else:
        raise ValueError("Invalid image ordering")

    cover_img = Image.new("RGB", (500, 230), color=(73, 109, 137))

    d = ImageDraw.Draw(cover_img)
    d.text((50, 50), title, fill=(255, 255, 255))

    images = [Image.open(f).convert("RGB") for f in image_files]

    cover_img.save(
        f"{title}.pdf",
        resolution=100.0,
        save_all=True,
        append_images=images,
    )


def _sequential(directories: List[str]):
    image_files_directories = [
        natsorted(glob.glob(f"{directory}/*.png")) for directory in directories
    ]

    result = []
    for image_files in image_files_directories:
        for image in image_files:
            result.append(image)

    return result


def _alternate_between(directories: List[str]):
    image_files_directories = [
        natsorted(glob.glob(f"{directory}/*.png")) for directory in directories
    ]

    if not len(set(map(len, image_files_directories))) == 1:
        raise ValueError("The number of images in each directory is not the same")

    result = []
    for i in range(len(image_files_directories[0])):
        for j in range(len(image_files_directories)):
            result.append(image_files_directories[j][i])
    return result


if __name__ == "__main__":
    directories = [
        "examples/alternate_between/questions",
        "examples/alternate_between/answers",
    ]
    to_pdf(title="examples", directories=directories)
