import requests
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"


def get_attachment_by_id(attachment_id):
    response = requests.get(url)
    if response.status_code == 200:
        response_data = response.json()
        # Recorre todos los posts
        for post in response_data['posts']:
            for attachment in post['attachments']:
                if attachment['id'] == attachment_id:
                    return attachment['title']
    return None

print(get_attachment_by_id(137))
