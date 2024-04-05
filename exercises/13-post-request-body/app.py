import requests

response = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php")
print(response.text)