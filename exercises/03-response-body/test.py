import json, pytest
from mock import patch

@pytest.mark.it("requests.get has to be called for the random-status.php url")
def test_url_call(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        mock_request.assert_called_once_with("https://assets.breatheco.de/apis/fake/sample/random-status.php")

@pytest.mark.it("Testing for 200: Everything went perfect")
def test_url_200(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.text = "something"
        app()
        captured = capsys.readouterr()
        assert "something\n" == captured.out

@pytest.mark.it("Testing for any other code: Something went wrong")
def test_url_404(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value.status_code = 404
        app()
        captured = capsys.readouterr()
        assert "Something went wrong\n" == captured.out