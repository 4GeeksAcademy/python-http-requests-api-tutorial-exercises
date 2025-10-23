import requests
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)
if response.status_code == 200:
    response_data = response.json()
    print(response_data)
    var = response_data['posts'][0]['author']['name']
    print(var)

# Your code here