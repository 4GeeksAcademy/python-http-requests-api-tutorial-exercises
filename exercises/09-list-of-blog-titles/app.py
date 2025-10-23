import requests
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"


def get_titles():
    title_list = []
    response = requests.get(url)
    if response.status_code == 200:
        response_data = response.json()
        for post in response_data['posts']:
            title_list.append(post['title'])
    return title_list

print(get_titles())


