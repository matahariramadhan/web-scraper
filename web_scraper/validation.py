import requests


class Validation:
    '''Act as middleware, it will return the value if the value is valid or raise exception'''

    def validate_url(self, url: str) -> str:
        try:
            status_code = requests.get(url).status_code
            if status_code == 200:
                return url
            raise Exception(f'Url is not valid')
        except:
            raise Exception(f'Url is not valid')
