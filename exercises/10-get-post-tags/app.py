import requests
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

def get_post_tags(post_id):
   
    response = requests.get(url)
    if response.status_code == 200:
        response_data = response.json()
        for post in response_data['posts']:
            if post['id'] == post_id:
                return post['tags']

    # Your code here
    return None


print(get_post_tags(146))