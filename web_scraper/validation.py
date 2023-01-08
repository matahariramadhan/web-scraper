import pathlib
import requests


def validate_url(func):
    '''Decorator to validate url'''
    def onDecorator(*args):
        try:
            url = args[0]
            if len(args) > 1:
                url = args[1]
            status_code = requests.get(url).status_code
            if status_code == 200:
                return func(*args)
            raise Exception(f'Url is not valid, status code: {status_code}')
        except:
            # need to add connection issue exception here
            raise Exception(f'Url is not valid')
    return onDecorator


def validate_filepath(func) -> str:
    '''Decorator to validate file path'''
    def onDecorator(*args):
        try:
            path = args[0]
            if len(args) > 1:
                path = args[1]
            with pathlib.Path(path).open('r'):
                pass
            return func(*args)
        except:
            raise Exception(f'Path is not valid')

    return onDecorator
