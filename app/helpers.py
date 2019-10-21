"""
imports
"""
from functools import reduce


def topics(repos: list) -> list:
    """
    gather all the topics for a each repo
    and return a list of the topics
    """
    tops = [repo['topics'] for repo in repos]
    result = list(reduce(lambda x, y: x + y, tops))
    return result


def languages(repos: list) -> set:
    """
    computes the number of languages accross
    all repos
    """
    langs = [repo['language'] for repo in repos]
    result = {lang.lower()
            for lang
            in langs
            if lang is not None and lang != ""}
    return result


def watchers(key: str, list_data: list) -> int:
    """
    computes the number of watchers/followers
    accross all repos
    """
    # key is used to determine where the watchers are from
    # either bitbucket or github
    total = sum(item[key] for item in list_data if item is not None)
    return total


def public_repos(repos: list, key: str) -> tuple:
    """
    computes the number of public repos
    separated by original and forked repos
    """
    orig_repos = []
    # key is used to determine where the repos are from
    # either bitbucket or github
    if key == 'bitbucket':
        orig_repos[:] = [repo
                for repo
                in repos
                if not repo['is_private'] and 'parent' not in repo]
        return (len(repos) - len(orig_repos)), len(orig_repos)
    else:
        orig_repos[:] = [repo
                for repo
                in repos
                if not repo['private'] and not repo['fork']]
        return (len(repos) - len(orig_repos)), len(orig_repos)
