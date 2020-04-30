import json, pytest
from mock import patch

class FakeResponse(object):
    # default response attributes
    status_code = 200
    def json(self):
        return {
            "posts": [
                { "title": 'R.I.P. Ruby on Rails. Thanks for everything.' }, 
                {"title": 'The fraud behind the C.A. of digital certificates is over'}, 
                {"title": 'Manteniendo las raices'}, 
                {"title":'DF Tech Meetup, ya es una realidad'}
            ]
        }

@pytest.mark.it("You seem to be returning None or not retuning anything")
def test_for_null(app):
    with patch('requests.get') as mock_request:
        from app import get_titles
        mock_request.return_value = FakeResponse()
        resp = get_titles()
        assert resp is not None

@pytest.mark.it("The function should have returned a list but returned something different")
def test_return_type(app):
    with patch('requests.get') as mock_request:
        from app import get_titles
        mock_request.return_value = FakeResponse()
        tags = get_titles()
        assert isinstance(tags, list)

@pytest.mark.it("Return a list of post titles like: ['title 1','title 2', 'title 3']")
def test_array_content(app):
    with patch('requests.get') as mock_request:
        from app import get_titles
        mock_request.return_value = FakeResponse()
        titles = ['R.I.P. Ruby on Rails. Thanks for everything.', 'The fraud behind the C.A. of digital certificates is over', 'Manteniendo las raices', 'DF Tech Meetup, ya es una realidad']
        assert titles == get_titles()
