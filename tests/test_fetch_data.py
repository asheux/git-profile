"""
imports
"""

from mock import patch

from app.fetch_data import SendRequest

class TestExternalRequest:
    """
    test suite for requests sent to an external api
    """
    def test_get_json_data_success(self, data):
        with patch('app.fetch_data.SendRequest.get_json_data') as m_data:
            m_data.return_value = data
            url = 'https://api.github.com/orgs/pygame/repos'

            sr = SendRequest()
            # Call the service, which will send a request to the server.i
            res_data, err = sr.get_json_data(url)

            assert (res_data, err) == data

    def test_get_json_data_failure(self, error):
        with patch('app.fetch_data.SendRequest.get_json_data') as m_data:
            m_data.return_value = error
            url = 'https://api.github.com/orgs/pytfffest/repos'

            sr = SendRequest()
            # Call the service, which will send a request to the server.
            res_data, err = sr.get_json_data(url)

            assert (res_data, err) == error
