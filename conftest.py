import pathlib
import pytest


@pytest.fixture
def markup() -> bytes:
    with pathlib.Path('tests/samples/markup.html').open('rb') as file:
        return file.read()


@pytest.fixture
def MockRequests(markup):
    '''Return mock object of requests'''
    class MockRequests:
        '''Mock requests module'''

        def __init__(self, markup) -> None:
            self.content = markup
            self.status_code: int

        def get(self):
            return self
    return MockRequests(markup)
