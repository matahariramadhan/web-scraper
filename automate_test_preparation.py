import pathlib
import requests


def create_markup_html(url):
    with pathlib.Path('tests/samples/markup.html').open('wb') as markup:
        markup.write(requests.get(url).content)


if __name__ == '__main__':
    url = 'https://shamela.ws/book/23599/612'
    try:
        create_markup_html(url)

        print('Successfully prepare test!')
    except Exception as e:
        print("ERROR PREPARING TEST!!!")
        print(e)
