"""
imports
"""
import os


GIT_CLIENT_ID = os.getenv('GIT_CLIENT_ID')
GIT_CLIENT_SECRET = os.getenv('GIT_CLIENT_SECRET')

BITBUCKET_BASE_URL = 'https://api.bitbucket.org'
GITHUB_BASE_URL = 'https://api.github.com'

HEADERS = {
        'content-type': 'application/json',
        'accept': 'Accept: application/vnd.github.v3+json, \
                application/vnd.github.mercy-preview+json'}
DEVELOPMENT = True
APP_DEBUG = True
