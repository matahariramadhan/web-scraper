from .scraper import Scraper


class ShamelaScraper(Scraper):
    def __init__(self, url: str) -> None:
        super().__init__(url)
