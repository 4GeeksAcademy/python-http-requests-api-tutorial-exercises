import requests

resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php")
print(resp.text)