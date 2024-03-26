import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"

data = {
    "id": 2323,
    "title": "Very big project"
}

# Setting the headers
headers = {
    "Content-Type": "application/json"
}

# Sending POST request with dictionary data
response = requests.post(url, json=data, headers=headers)

print(response.text)