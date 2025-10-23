import requests
url = "https://assets.breatheco.de/apis/fake/sample/post.php"

response = requests.post(url)
print(response.text)
