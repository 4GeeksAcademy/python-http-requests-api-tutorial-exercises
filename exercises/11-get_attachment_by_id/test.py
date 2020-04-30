import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return {
            "posts": [
                { "attachments": [{ "id": 22, "title": "asd" }] }, 
                { "attachments": [{ "id": 137, "title": "cert" }] }, 
                { "attachments": [{ "id": 11, "title": "asd" }] }, 
                { "attachments": [{ "id": 40, "title": "asd" }] }, 
                { "attachments": [{ "id": 314, "title": "asd" }] }, 
            ]
        }

@pytest.mark.it("You seem to be returning None or not retuning anything on the function")
def test_for_null(app):
    with patch('requests.get') as mock_request:
        from app import get_attachment_by_id
        mock_request.return_value = FakeResponse()
        att = get_attachment_by_id(137)
        assert att is not None

@pytest.mark.it("The function should have returned a string (the att title) but returnied something different")
def test_return_type(app):
    with patch('requests.get') as mock_request:
        from app import get_attachment_by_id
        mock_request.return_value = FakeResponse()
        title = get_attachment_by_id(137)
        assert isinstance(title, str)

@pytest.mark.it("Return the attachment title")
def test_array_content(app):
    with patch('requests.get') as mock_request:
        from app import get_attachment_by_id
        mock_request.return_value = FakeResponse()
        title = get_attachment_by_id(137)
        assert title == "cert"
