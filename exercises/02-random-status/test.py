import json, pytest
from mock import patch

@pytest.mark.it("requests.get has to be called for the random-status.php url")
def test_url_call(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        mock_request.assert_called_once_with("https://assets.breatheco.de/apis/fake/sample/random-status.php")


@pytest.mark.it("Testing for 200: Everythign went perfect")
def test_url_200(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value.status_code = 200
        app()
        captured = capsys.readouterr()
        assert "Everything went perfect\n" == captured.out

@pytest.mark.it("When testing for 404 it should print The URL you asked is not found'")
def test_url_404(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value.status_code = 404
        app()
        captured = capsys.readouterr()
        assert "The URL you asked is not found\n" == captured.out

@pytest.mark.it("Testing for 503: Unavailable right now")
def test_url_503(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value.status_code = 503
        app()
        captured = capsys.readouterr()
        assert "Unavailable right now\n" == captured.out

@pytest.mark.it("Testing for 400: Something is wrong on the request params")
def test_url_400(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value.status_code = 400
        app()
        captured = capsys.readouterr()
        assert "Something is wrong on the request params\n" == captured.out
