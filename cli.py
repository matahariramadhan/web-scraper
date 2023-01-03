import pathlib
from web_scraper import Parser, ShamelaParser, Fetcher, XMLSaver, Scraper
from tqdm import trange


def scrape(url: str, output_path: str):
    scraper = Scraper(Fetcher, ShamelaParser, XMLSaver)

    scraper.fetch_from_internet(url).parse_content().save(output_path)


def main():
    print('Welcome to web scraper by Matahari Ramadhan')
    print('==========================================\n')
    url = input('Enter url: ')
    output = input('Enter output path: ')
    scrape(url, output)


# url = 'https://shamela.ws/book/23599/612'
if __name__ == '__main__':
    # scrape(str(
    #     pathlib.Path('samples/').resolve()))
    main()
