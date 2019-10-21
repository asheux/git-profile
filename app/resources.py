"""
imports
"""

from flask_restful import Resource
from flask import jsonify

from .compute_data import BitBucket, GitHub
from . import api


class GitProfile(Resource):
    """
    This class aggrates data from both Github and
    Bitbucket APIs to present information in a unified
    response
    """
    def get(self, organization):
        # instances
        github = GitHub(organization)
        bitbucket = BitBucket(organization)
        # errors
        errors = [error
                for error
                in [bitbucket.error,github.error]
                if error is not None
                ]
        if len(errors) == 0:
            b_langs, bw_count, bo_count, bf_count = bitbucket.bit_results()
            t_count, gw_count, g_langs, gf_count, go_count = github.git_results()
            merged_data = {
                    'public_repos': {
                        'original_repos': bo_count + go_count,
                        'forked_repos': bf_count + gf_count
                        },
                    'languages': list(b_langs | g_langs),
                    'watchers': bw_count + gw_count,
                    'topics': t_count,
                    }
            return jsonify({'result': merged_data})
        return jsonify({'errors': errors})

api.add_resource(GitProfile, '/repos/<string:organization>')
