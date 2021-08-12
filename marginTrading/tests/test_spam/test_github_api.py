from unittest.mock import Mock

from marginTrading import github_api


def teste_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'sambiase', 'id': 78605825, 'node_id': 'MDQ6VXNlcjc4NjA1ODI1',
                                   'avatar_url': 'https://avatars.githubusercontent.com/u/78605825?v=4'}
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('sambiase')
    assert 'https://avatars.githubusercontent.com/u/78605825?v=4' == url