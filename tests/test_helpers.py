"""
imports
"""
from mock import patch

from app.helpers import topics, languages, watchers, public_repos
from .mock_data import REPOS


class TestHelpers:
    def test_topics(self, topics_result):
        with patch('app.helpers.topics') as m_data:
            m_data.return_value = topics_result
            tops = topics(REPOS)
            assert tops == topics_result

    def test_languages(self, languages_result):
        with patch('app.helpers.languages') as m_data:
            m_data.return_value = languages_result
            langs = languages(REPOS)
            assert langs == languages_result 

    def test_watchers(self, watchers_result):
        with patch('app.helpers.watchers') as m_data:
            m_data.return_value = watchers_result
            w = watchers('watchers_count', REPOS)
            assert w == watchers_result

    def test_public_repos(self, public_repos_result):
        with patch('app.helpers.public_repos') as m_data:
            m_data.return_value = public_repos_result
            p_repos = public_repos(REPOS, 'github')
            assert p_repos == public_repos_result
