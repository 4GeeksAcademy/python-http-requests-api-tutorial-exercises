import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    content = '{"hours":"19","minutes":"45","seconds":"06"}'
    def json(self):
        return {"hours":"19","minutes":"45","seconds":"06"}

@pytest.mark.it("requests.get has to be called for the time.php url")
def test_url_call(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        mock_request.assert_called_once_with("https://assets.breatheco.de/apis/fake/sample/time.php")

@pytest.mark.it("You should print on the console a stirng like: Current time: 19 hrs 45 min and 06 sec")
def test_url_output(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value = FakeResponse()
        app()
        captured = capsys.readouterr()
        assert "Current time: 19 hrs 45 min and 06 sec\n" == captured.out