import requests
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
if response.status_code == 200:
    response_data = response.json()
    var = response_data[-1]["images"][2]
    print(var)

# Your code here