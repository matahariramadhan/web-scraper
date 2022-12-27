import pathlib
from web_scraper import ShamelaScraper as Shamela
from web_scraper import Fetcher
import time
from tqdm import trange


def auto_scraper_xml(scraper, start: str, end: str):
    def inner(base_url: str, output_path: str):
        for n in trange(start, end+1):
            time.sleep(0.5)
            scraper.parse_from_url(base_url+str(n)).save_to_xml(
                output_path, str(n) + '.xml')
    return inner


def main():
    base_url = 'https://shamela.ws/book/23599/'
    shamela = Shamela()

    shamela_scraper = auto_scraper_xml(shamela, 612, 613)
    shamela_scraper(base_url, output_path=str(
        pathlib.Path('samples/').resolve()))


if __name__ == '__main__':
    main()
