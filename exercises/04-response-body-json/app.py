import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
#print(response.text)
response_json = response.json()
#print("The response status is: "+str(response.status_code))
#print(response_json)
print(f"Current time: {response_json['hours']} hrs {response_json['minutes']} min and {response_json['seconds']} sec")