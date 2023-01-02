import pathlib
import requests


def automate_test_preparation():
    url = 'https://shamela.ws/book/23599/612'

    raw_html = requests.get(url).content

    with pathlib.Path('tests/samples/markup.html').open('wb') as markup:
        markup.write(raw_html)


if __name__ == '__main__':
    automate_test_preparation()
