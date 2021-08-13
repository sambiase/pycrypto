import pytest as pytest
from unittest.mock import Mock

from marginTrading import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/78605825?v=4'
    resp_mock.json.return_value = {'login': 'sambiase', 'id': 78605825, 'node_id': 'MDQ6VXNlcjc4NjA1ODI1',
                                   'avatar_url': url}
    get_mock = mocker.patch('marginTrading.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url



def teste_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('sambiase')
    assert avatar_url == url


def teste_buscar_avatar_integracao():
    url = github_api.buscar_avatar('sambiase')
    assert 'https://avatars.githubusercontent.com/u/78605825?v=4' == url