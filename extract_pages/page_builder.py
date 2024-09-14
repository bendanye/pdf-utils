from typing import List


class PageBuilder:
    _pages: List

    def __init__(self, pages: List = []):
        self._pages = pages

    def add_page_single(self, page: int):
        self._pages.append(page)
        return PageBuilder(self._pages)

    def add_page_range(self, from_page: int, to_page: int):
        if from_page > to_page:
            raise ValueError("to_page cannot be smaller than from_page")

        for page in range(from_page, to_page + 1):
            self._pages.append(page)

        return PageBuilder(self._pages)

    def build(self):
        return self._pages
