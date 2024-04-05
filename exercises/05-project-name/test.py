import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return {
            "name": "Sample Project",
            "thumb": "https://unsplash.it/450/320?image=178",
            "description": "The coolest eLearning site on the planet",
            "images": [
                "https://unsplash.it/450/320?image=178",
                "https://unsplash.it/450/320?image=179",
                "https://unsplash.it/450/320?image=180",
                "https://unsplash.it/450/320?image=181"
            ]
        }

@pytest.mark.it("requests.get has to be called for the project.php url")
def test_url_call(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        mock_request.assert_called_once_with("https://assets.breatheco.de/apis/fake/sample/project1.php")


@pytest.mark.it("You should print the name of the project on the console")
def test_url_output(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value = FakeResponse()
        app()
        captured = capsys.readouterr()
        assert "Sample Project\n" == captured.out