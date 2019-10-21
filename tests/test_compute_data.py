'''
imports
'''
from mock import patch
from app.compute_data import BitBucket, GitHub


class TestBitBucket:
    """
    test suite for computed bitbucket data
    """
    def test_bitbucket_data(self, bb_results):
        with patch('app.compute_data.BitBucket.bit_results') as mock_data:
            mock_data.return_value = bb_results

            b = BitBucket('pygame')
            result = b.bit_results()
            assert result == bb_results


class TestGitHub:
    """
    test suite for computed github data
    """
    def test_github_data(self, g_results):
        with patch('app.compute_data.GitHub.git_results') as mock_data:
            mock_data.return_value = g_results

            g = GitHub('pygame')
            result = g.git_results()
            assert result == g_results

