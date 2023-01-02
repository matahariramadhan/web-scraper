import pathlib
from web_scraper import Parser, ShamelaParser, Fetcher, XMLSaver, Scraper
from tqdm import trange


def scrape(output_path: str):
    url = 'https://shamela.ws/book/23599/612'
    scraper = Scraper(Fetcher, ShamelaParser, XMLSaver(output_path))

    scraper.fetch_from_internet(url).parse_content().save()


if __name__ == '__main__':
    scrape(str(
        pathlib.Path('samples/').resolve()))
