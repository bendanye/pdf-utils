from dataclasses import dataclass


@dataclass
class PageRange:
    from_page: int
    to_page: int
