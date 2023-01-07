import pathlib
import requests
from web_scraper import Scraper, Fetcher, ShamelaParser, XMLSaver
from bs4 import BeautifulSoup


def create_markup_html(url):
    with pathlib.Path('tests/samples/markup.html').open('wb') as markup:
        markup.write(requests.get(url).content)


def create_result_xml(url, output_path):
    scraper = Scraper(Fetcher, ShamelaParser, XMLSaver)
    scraper.fetch_from_internet(url).parse_content().save(output_path)


def create_nass_dict(url):
    raw_html = Fetcher().fetch_from_internet(url)
    soup = BeautifulSoup(raw_html, 'html.parser')
    nass = soup.find('div', class_='nass')

    with pathlib.Path('tests/samples/nass.txt').open('w') as file:
        file.write(str(nass))


if __name__ == '__main__':
    url = 'https://shamela.ws/book/23599/612'
    try:
        create_markup_html(url)
        create_result_xml(
            url, '/home/matahari/development/projects/web-scraping/tests/samples')
        create_nass_dict(url)

        print('Successfully prepare test!')
    except Exception as e:
        print("ERROR PREPARING TEST!!!")
        print(e)
