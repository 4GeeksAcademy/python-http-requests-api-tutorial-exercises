import requests

url = "https://assets.breatheco.de/apis/fake/sample/404-example.php"
response = requests.get(url)

print("The response status is: "+str(response.status_code))