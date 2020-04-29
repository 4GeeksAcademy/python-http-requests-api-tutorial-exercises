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

@pytest.mark.it("Make sure you are printing the author name of the FIRST post")
def test_array_content(app):
    with patch('requests.get') as mock_request:
        from app import get_titles
        mock_request.return_value = FakeResponse()
        titles = ['R.I.P. Ruby on Rails. Thanks for everything.', 'The fraud behind the C.A. of digital certificates is over', 'Manteniendo las raices', 'DF Tech Meetup, ya es una realidad']
        assert titles == get_titles()
