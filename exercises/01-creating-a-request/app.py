import requests

"""url = "https://assets.breatheco.de/apis/fake/sample/hello.php"
 
response = requests.get(url)

print("The response status is: "+str(response.status_code))"""





url = "https://assets.breatheco.de/apis/fake/sample/hello.php"
 
response = requests.get(url)
print("Codigo de estado:")
print(response.status_code) # para obtener el código de estado
print("\nCuerpo de la respuesta en formato texto:")
print(response.text)       # para obtener el cuerpo de la pagina en formato texto
print("\nCuerpo de la respuesta en formato binario:")
print(response.content)    # para obtener el cuerpo de la pagina en formato binario
print("\nCuerpo de la respuesta en formato json:")
print(response.json())    # para obtener el cuerpo de la pagina en formato json

"""response = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php")
print(response.text)""" # para enviar una solicitud POST y ver la respuesta en formato texto