import pathlib

import requests
from web_scraper import validation
import pytest


class TestValidateUrl:
    @pytest.fixture
    def valid_url(self) -> str:
        return 'https://shamela.ws/book/23599/612'

    def test_validate_url_pass(self, valid_url, MockRequests, monkeypatch):
        # Mocking get method from requests
        def mock_get(*args, **kwargs):
            MockRequests.status_code = 200
            return MockRequests.get()
        monkeypatch.setattr(
            requests, 'get', mock_get)

        @validation.validate_url
        def func(valid_url):
            return valid_url
        actual = func(valid_url)
        expected = 'https://shamela.ws/book/23599/612'

        assert actual == expected

    def test_validate_url_raise_exception(self, MockRequests, monkeypatch):
        # need to parameterize this test to many exception
        # Mocking get method from requests
        def mock_get(*args, **kwargs):
            MockRequests.status_code = 404
            return MockRequests.get()
        monkeypatch.setattr(
            requests, 'get', mock_get)

        with pytest.raises(Exception) as e:
            @validation.validate_url
            def func(valid_url):
                '''dummy func'''
            func('https://shamela.ws/book/23599/6120')
        assert str(e.value) == 'Url is not valid'


class TestValidateFilePath:
    @pytest.fixture
    def valid_filepath(self, tmp_path):
        filepath = tmp_path/'test.txt'
        with pathlib.Path(filepath).open('w') as file:
            file.write('')
        return filepath

    def test_validate_path_pass(self, valid_filepath):
        @validation.validate_filepath
        def func(path):
            '''Dummy func'''
            return path

        actual = func(valid_filepath)
        expected = valid_filepath
        assert actual == expected

    def test_validate_path_raise_exception(self):
        with pytest.raises(Exception) as e:
            @validation.validate_filepath
            def func(self, path):
                '''dummy func that has 2 parameter'''
            func(self, '/dummy')
        assert str(e.value) == 'Path is not valid'
