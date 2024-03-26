import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return {
            "posts": [
                { "attachments": [{ "id": 22, "title": "Invoice" }] }, 
                { "attachments": [{ "id": 137, "title": "Training Certificate" }] }, 
                { "attachments": [{ "id": 11, "title": "Presentation Slides" }] }, 
                { "attachments": [{ "id": 40, "title": "Meeting Agenda" }] }, 
                { "attachments": [{ "id": 314, "title": "Project Proposal" }] }, 
            ]
        }

@pytest.mark.it("You seem to be returning None or not returning anything on the function")
def test_for_null(app):
    with patch('requests.get') as mock_request:
        from app import get_attachment_by_id
        mock_request.return_value = FakeResponse()
        att = get_attachment_by_id(137)
        assert att is not None

@pytest.mark.it("The function should have returned a string (the attachment title) but returned something different")
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
        assert title == "Training Certificate"
