import json, pytest
from mock import patch

@pytest.mark.it("POST request to the specified endpoint")
def test_url(app):
    with patch('requests.post') as mock_request:
        app()
        url = "https://assets.breatheco.de/apis/fake/sample/post.php"
        assert mock_request.call_args.args[0] == url

@pytest.mark.it("Print the response text in the console")
def test_print(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        captured = capsys.readouterr()
        assert captured.out.find("Excelent") > 0