import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

if response.status_code == 404:
    print("The URL you asked for is not found")
elif response.status_code == 503:
    print("Unavailable right now")
elif response.status_code == 200:
    print("Everything went perfect")
elif response.status_code == 400:
    print("Something is wrong with the request params")
else:
    print("Unknown status code")