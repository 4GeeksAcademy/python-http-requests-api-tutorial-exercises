import requests
url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
 
response = requests.get(url)


response_data = response.json()
print(response_data['name'])
# Your code here