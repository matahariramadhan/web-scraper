import pathlib
import requests
from web_scraper import Scraper, Fetcher, ShamelaParser, XMLSaver


def create_markup_html():
    url = 'https://shamela.ws/book/23599/612'

    raw_html = requests.get(url).content

    with pathlib.Path('tests/samples/markup.html').open('wb') as markup:
        markup.write(raw_html)


def create_result_xml(url, output_path):
    scraper = Scraper(Fetcher, ShamelaParser, XMLSaver)
    scraper.fetch_from_internet(url).parse_content().save(output_path)


if __name__ == '__main__':
    try:
        create_markup_html()
        create_result_xml('https://shamela.ws/book/23599/612',
                          '/home/matahari/development/projects/web-scraping/tests/samples')

        print('Successfully prepare test!')
    except:
        print("ERROR PREPARING TEST!!!")
