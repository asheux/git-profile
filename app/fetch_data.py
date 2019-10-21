"""
imports
"""
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor

from requests.exceptions import ConnectionError

from .settings import GITHUB_BASE_URL, BITBUCKET_BASE_URL, HEADERS


class SendRequest:
    """
    This class's job is to send and handle
    requests sent to the remote server
    """
    @classmethod
    def get_data(cls, url): 
        """
        make requests to a remote server
        """
        data = None
        error = None
        try:
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                data = response.json()
            else:
                error = response.json()
        except ConnectionError:
            print('Connection refused')
        return data, error

    @classmethod
    def get_bitbucket(cls, organization):
        url = f"{BITBUCKET_BASE_URL}/2.0/repositories/{organization}"
        return cls.get_data(url)

    @classmethod
    def get_github(cls, organization):
        url = f"{GITHUB_BASE_URL}/orgs/{organization}/repos"
        return cls.get_data(url)

    @classmethod
    def generate_links(cls, repos):
        """
        For each repository from the list of repo urls
        produce a link to fetch data and return
        :params: list of repos
        :return: generator
        """
        for repo in repos:
            yield repo['links']['watchers']['href']

    @classmethod
    async def run_tasks(
            cls,
            repos,
            executor, 
            event_loop):
        """
        runs blocking tasks asyncronously
        """
        blocking_tasks = [
                event_loop.run_in_executor(executor, cls.get_data, url)
                for url in cls.generate_links(repos) 
                ]
        completed, pending = await asyncio.wait(blocking_tasks)
        results = [task.result() for task in completed]
        return results

    @classmethod
    def start_request(cls, repos):
        """
        runs all the requests concurrently
        """
        # the ThreadPoolExecutor class will be used with the 
        # default number of threads 
        # (the number of processors multiplied by 5)
        with ThreadPoolExecutor() as exe:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(cls.run_tasks(repos, exe, loop))
        return result

