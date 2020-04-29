import json, pytest
from mock import patch

@pytest.mark.it("Update the url to hello.php")
def test_url(app):
    with patch('requests.get') as mock_request:
        app()
        url = "https://assets.breatheco.de/apis/fake/hello.php"
        assert mock_request.call_args.args[0] == url