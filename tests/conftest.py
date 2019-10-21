import pytest


@pytest.fixture()
def bb_results():
    return {'python', 'c++'}, 11, 7, 0


@pytest.fixture()
def g_results():
    return 8, 6, {'python', 'ruby', 'c'}, 1, 5


@pytest.fixture()
def topics_result():
    return ['data', 'ai', 'ml', 'humans', 'robots']


@pytest.fixture()
def languages_result():
    return {'c++', 'c', 'ruby', 'python'}

@pytest.fixture()
def watchers_result():
    return 211


@pytest.fixture()
def public_repos_result():
    return 2, 3


@pytest.fixture()
def data():
    return ('<Response [200]>', None)


@pytest.fixture()
def error():
    return (None, '<Response [404]>')
