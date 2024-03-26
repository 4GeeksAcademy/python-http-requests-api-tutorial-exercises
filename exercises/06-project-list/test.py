import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return [{
            "name": "Starbucks for milkshakes",
            "thumb": "https://unsplash.it/450/320?image=178",
            "description": "",
            "images": [
                "https://unsplash.it/450/320?image=178",
                "https://unsplash.it/450/320?image=179",
                "https://unsplash.it/450/320?image=180",
                "https://unsplash.it/450/320?image=181"
            ]
        },
        {
            "name": "Uber for trucks",
            "thumb": "https://unsplash.it/450/320?image=178",
            "description": "",
            "images": [
                "https://unsplash.it/450/320?image=178",
                "https://unsplash.it/450/320?image=179",
                "https://unsplash.it/450/320?image=180",
                "https://unsplash.it/450/320?image=181"
            ]
        },
        {
            "name": "McDonalds for tacos",
            "thumb": "https://unsplash.it/450/320?image=178",
            "description": "",
            "images": [
                "https://unsplash.it/450/320?image=178",
                "https://unsplash.it/450/320?image=179",
                "https://unsplash.it/450/320?image=180",
                "https://unsplash.it/450/320?image=181"
            ]
        }
    ]

@pytest.mark.it("requests.get has to be called for the project_list.php url")
def test_url_call(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        mock_request.assert_called_once_with("https://assets.breatheco.de/apis/fake/sample/project_list.php")

@pytest.mark.it("The printed position should be 1 (not 2 because lists indexes start at 0)")
def test_url_output2(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value = FakeResponse()
        app()
        captured = capsys.readouterr()
        assert "McDonalds for tacos\n" != captured.out

@pytest.mark.it("Make sure you are printing the project name")
def test_url_output1(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value = FakeResponse()
        app()
        captured = capsys.readouterr()
        assert "Uber for trucks\n" == captured.out
