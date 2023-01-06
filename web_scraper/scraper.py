from web_scraper import Fetcher, Parser, Saver


class Scraper:
    '''Scraper fetch data from internet then parse and save it.

    Dependency: Fetcher, Parser, Saver'''

    def __init__(self, fetcher: Fetcher, parser: Parser, saver: Saver) -> None:
        self.fetcher = fetcher
        self.parser = parser
        self.saver = saver
        self.markup: bytes | str = bytes()
        self.content: dict = {}

    def fetch_from_internet(self, url: str):
        '''Fetch data from internet then populate self.markup.

        Return scraper object it self'''
        raw_html = self.fetcher().fetch_from_internet(url)
        self.markup = raw_html
        return self

    def fetch_from_local(self):
        pass

    def parse_content(self):
        '''Take self.markup and parse the content then populate self.content.'''
        self.content = self.parser().parse_content(self.markup)
        return self

    def save(self, output_path: str, output_filename: str = 'result') -> None:
        '''Take self.content and save it to output_path'''
        self.saver().save(self.content, output_path, output_filename)
