import json, pytest
from mock import patch

@pytest.mark.it("Make a POST request to the specified endpoint")
def test_url(app):
    with patch('requests.post') as mock_request:
        app()
        url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"
        assert mock_request.call_args.args[0] == url

@pytest.mark.it("Request header content-type must be application/json")
def test_headers(app):
    with patch('requests.post') as mock_request:
        app()
        assert "headers" in mock_request.call_args.kwargs
        assert "Content-Type" in mock_request.call_args.kwargs["headers"] or "content-type" in mock_request.call_args.kwargs["headers"]

        headers = mock_request.call_args.kwargs["headers"]
        if "Content-Type" in headers:
            assert headers["Content-Type"].lower() == "application/json"
        if "content-type" in headers:
            assert headers["content-type"].lower() == "application/json"

@pytest.mark.it("Request body must be a json object with id and title")
def test_body(app):
    with patch('requests.post') as mock_request:
        app()
        assert "json" in mock_request.call_args.kwargs

        body = mock_request.call_args.kwargs["json"]
        assert "id" in body
        assert "title" in body