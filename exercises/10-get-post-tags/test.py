import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return {
            "posts": [
                { "id": 234, "tags": [
                        { "id": 25, "title": "programming" },
                        { "id": 26, "title": "software development"}
                    ] 
                }, 
                { "id": 224, 
                    "tags": [
                        { "id": 23, "title": "react" },
                        { "id": 11, "title": "cooking"}
                    ] 
                }, 
                { "id": 14, "tags": [] }, 
                { "id": 34, "tags": [] }, 
                { "id": 24, "tags": [] }, 
            ]
        }

@pytest.mark.it("You seem to be returning None or not retuning anything")
def test_for_null(app):
    with patch('requests.get') as mock_request:
        from app import get_post_tags
        mock_request.return_value = FakeResponse()
        tags = get_post_tags(224)
        assert tags is not None

@pytest.mark.it("The function should have returned a list but returned something different")
def test_return_type(app):
    with patch('requests.get') as mock_request:
        from app import get_post_tags
        mock_request.return_value = FakeResponse()
        tags = get_post_tags(224)
        assert isinstance(tags, list)

@pytest.mark.it("Given the post id, return a list with the post tags given")
def test_array_content(app):
    with patch('requests.get') as mock_request:
        from app import get_post_tags
        mock_request.return_value = FakeResponse()

        tags = get_post_tags(224)

        assert len(tags) == 2
        assert tags[0]["id"] == 23
        assert tags[1]["id"] == 11
