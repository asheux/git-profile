"""
imports
"""
from .fetch_data import SendRequest
from .helpers import topics, languages, watchers, public_repos
from .settings import GITHUB_BASE_URL as G, BITBUCKET_BASE_URL as B


class BitBucket(SendRequest):
    """
    This class handles repos only stored on bitbucket
    """
    def __init__(self, orgs):
        self.orgs = orgs
        self.url = f"{B}/2.0/repositories/{self.orgs}"
        self.res, self.error = self.get_json_data(self.url)

    def bit_results(self):
        """
        merge all the computed results for bitbucket
        """
        repos = self.res['values']

        # bitbucket provides a url to fetch watchers/followers
        # therefore we need to pull out all the urls and fetch 
        # watchers concurrently
        fetched_watchers = self.run_process(repos)
        watchers_count = watchers('size', fetched_watchers)
        f_count, o_count = public_repos(repos, 'bitbucket')
        b_langs = languages(repos)

        return b_langs, watchers_count, o_count, f_count


class GitHub(SendRequest):
    """
    This class handles repos only stored on github
    """
    def __init__(self, orgs):
        self.orgs = orgs
        self.url = f"{G}/orgs/{self.orgs}/repos"
        self.repos, self.error = self.get_json_data(self.url)

    def git_results(self):
        """
        merge all the computed results for github
        """
        watchers_count = watchers('watchers_count', self.repos)
        g_langs = languages(self.repos)
        f_count, o_count = public_repos(self.repos, 'github')
        topic_count = len(topics(self.repos)) 

        return topic_count, watchers_count, g_langs, f_count, o_count

