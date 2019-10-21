"""
imports
"""
import aiohttp
import requests
import asyncio

from requests.exceptions import ConnectionError

from .settings import HEADERS


class SendRequest:
    """
    This class's job is to send and handle
    requests sent to the remote server
    """
    def get_json_data(self, url): 
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

    def generate_links(self, repos: list):
        """
        For each repository from the list of repo urls
        produce a link to fetch data and return
        :params: list of repos
        :return: generator
        """
        for repo in repos:
            yield repo['links']['watchers']['href']

    async def get_data(self, session: aiohttp.ClientSession, url):
        """
        since the tasks involved are I/O bound
        the method will have to be asyncronous and
        it's not using requests library to fetch data because
        the library does not support asynchronous I/O with
        async and await keywords
        :return: coroutine
        """
        async with session.get(url) as response:
            return await response.json()

    async def fetch_data(self, session, url):
        return await self.get_data(session, url)

    async def run_tasks(self, repos):
        """
        runs blocking tasks and returns the completed
        one with the actual data
        """
        async with aiohttp.ClientSession() as session:
            blocking_tasks = [
                    self.fetch_data(session, url)
                    for url in self.generate_links(repos)]
            completed, pending = await asyncio.wait(blocking_tasks)
            results = [task.result() for task in completed]
            return results

    def run_process(self, repos: list):
        """
        runs all the requests concurrently
        using event loop that dispatches each event
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.run_tasks(repos))
        return result

