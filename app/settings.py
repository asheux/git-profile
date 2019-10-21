"""
imports
"""
import os

BITBUCKET_BASE_URL = 'https://api.bitbucket.org'
GITHUB_BASE_URL = 'https://api.github.com'

# added Accept media type for API version explicitely for stability
# since the default version of the external API may change in the future
# The preview Accept media type is for us to get all the list of
# topics for each repos as per github API
HEADERS = {
        'content-type': 'application/json',
        'accept': 'Accept: application/vnd.github.v3+json, \
                application/vnd.github.mercy-preview+json'}
DEVELOPMENT = True
TESTING = True
APP_DEBUG = True
