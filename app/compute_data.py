"""
imports
"""
from .fetch_data import SendRequest
from .helpers import topics, languages, watchers, public_repos


class BitBucket(SendRequest):
    """
    This class handles repos only stored on bitbucket
    """
    def __init__(self, orgs):
        self.orgs = orgs
        self.res, self.error = self.get_bitbucket(self.orgs)

    def bit_results(self):
        """
        merge all the computed results for bitbucket
        """
        repos = self.res['values']
        fetched_watchers = self.start_request(repos)
        fetched_watchers[:] = [repo[0]
                for repo in fetched_watchers if repo is not None]

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
        self.repos, self.error = self.get_github(orgs)

    def git_results(self):
        """
        merge all the computed results for github
        """
        watchers_count = watchers('watchers_count', self.repos)
        g_langs = languages(self.repos)
        f_count, o_count = public_repos(self.repos, 'github')
        topic_count = len(topics(self.repos)) 

        return topic_count, watchers_count, g_langs, f_count, o_count

