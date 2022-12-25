import pathlib
from web_scraper import ShamelaScraper as Shamela


def main():
    url = 'https://shamela.ws/book/23599/611'
    shamela = Shamela(url)

    shamela.save_to_html(pathlib.Path('samples').resolve())


if __name__ == '__main__':
    main()
