from web_scraper import Fetcher, Parser, Saver


class Scraper:
    '''Abstract class (interface) of scraper'''

    def __init__(self, fetcher: Fetcher, parser: Parser, saver: Saver) -> None:
        self.fetcher = fetcher
        self.parser = parser
        self.saver = saver
        self.markup: bytes | str = bytes()
        self.content: dict = {}

    def fetch_from_internet(self, url: str):
        raw_html = self.fetcher().fetch_from_internet(url)
        self.markup = raw_html
        return self

    def fetch_from_local(self):
        pass

    def parse_content(self):
        self.content = self.parser().parse_content(self.markup)
        return self

    def save(self, output_path: str, output_filename='result.xml') -> None:
        self.saver().save(self.content, output_path, output_filename)
