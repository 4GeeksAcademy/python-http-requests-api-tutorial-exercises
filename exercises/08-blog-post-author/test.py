import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return {
            "posts": [
                { "author": { "name": "octabio", "id": "12" } }
            ]
        }

@pytest.mark.it("requests.get has to be called for the weird_portfolio.php url")
def test_url_call(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        mock_request.assert_called_once_with("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

@pytest.mark.it("Make sure you are printing the author name of the FIRST post")
def test_url_output1(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value = FakeResponse()
        app()
        captured = capsys.readouterr()
        assert "octabio\n" == captured.out
