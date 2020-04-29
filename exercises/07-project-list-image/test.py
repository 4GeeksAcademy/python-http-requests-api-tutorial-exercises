import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return [
        {
            "name" : "Amazon eCommerce",
            "thumb" : "https://unsplash.it/450/320?image=778",
            "description" : "This website is an eCommerce made to sell books online",
            "images" : [
                "https://unsplash.it/450/320?image=778",
                "https://unsplash.it/450/320?image=779",
            ]
        },
        {
            "name" : "Coursera eLearning",
            "thumb" : "https://unsplash.it/450/320?image=178",
            "description" : "The coolest elarning site on the planet",
            "images" : [
                "https://unsplash.it/450/320?image=178",
                "https://unsplash.it/450/320?image=179",
                "https://unsplash.it/450/320?image=180",
                "https://unsplash.it/450/320?image=181"
            ]
        },
        {
            "name" : "Company Website",
            "thumb" : "https://unsplash.it/450/320?image=278",
            "description" : "Super boring company porfolio website with the tipical about us, home, contact us sections",
            "images" : [
                "https://unsplash.it/450/320?image=278",
                "https://unsplash.it/450/320?image=280",
                "https://image.shutterstock.com/image-vector/trophy-cup-award-vector-icon-260nw-592525184.jpg"
            ]
        }
    ]

@pytest.mark.it("requests.get has to be called to the project url")
def test_url_call(capsys, app):
    with patch('requests.get') as mock_request:
        app()
        mock_request.assert_called_once_with("https://assets.breatheco.de/apis/fake/sample/project_list.php")

@pytest.mark.it("Make sure you are printing the LAST image of the LAST project")
def test_url_output1(capsys, app):
    with patch('requests.get') as mock_request:
        mock_request.return_value = FakeResponse()
        app()
        captured = capsys.readouterr()
        assert "https://image.shutterstock.com/image-vector/trophy-cup-award-vector-icon-260nw-592525184.jpg\n" == captured.out
