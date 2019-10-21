"""
imports
"""

from flask_restful import Resource
from flask import jsonify

from .compute_data import BitBucket, GitHub


class GitProfile(Resource):
    """
    This class aggrates data from both Github and 
    Bitbucket APIs to present information in a unified
    response
    """
    def get(self, organization):

        github = GitHub(organization)
        bitbucket = BitBucket(organization)
        b_langs, bw_count, bo_count, bf_count = bitbucket.bit_results()
        t_count, gw_count, g_langs, gf_count, go_count = github.git_results()

        total_watchers = bw_count + gw_count
        langs_set = b_langs | g_langs
        total_forks = bf_count + gf_count
        total_originals = bo_count + go_count

        merged_data = {
                'public_repos': {
                    'original_repos': total_originals,
                    'forked_repos': total_forks
                    },
                'languages': len(langs_set),
                'watchers': total_watchers,
                'topics': t_count
                }

        return jsonify({'result': merged_data})






