import pathlib
from web_scraper import ShamelaScraper as Shamela
from web_scraper import Fetcher
import time
from tqdm import trange


def scrape(output_path: str):
    base_url = 'https://shamela.ws/book/23599/612'
    shamela = Shamela()

    shamela.parse_from_url(base_url).save_to_xml(output_path)


if __name__ == '__main__':
    scrape(str(
        pathlib.Path('samples/').resolve()))
