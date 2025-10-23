import requests
url="https://assets.breatheco.de/apis/fake/sample/save-project-json.php"
myjob = {"id": 2323, "title": "Very big project"}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=myjob, headers=headers)
print(response.text)


"""¿Qué son los Headers?
Los headers son como etiquetas que le dices al servidor qué tipo de información le estás enviando.

Content-Type: application/json
Es como decirle al servidor:

"Oye, los datos que te estoy enviando están en formato JSON"

Analogía sencilla:
Imagina que envías un paquete por correo:

SIN Content-Type:

Envías una caja cerrada
El cartero no sabe qué hay adentro
Puede que no sepa cómo manejarla
CON Content-Type:

Pones una etiqueta: "FRÁGIL - CRISTAL"
Ahora el cartero sabe exactamente cómo tratarla

Los headers se usan para diferentes propósitos dependiendo del tipo de petición:
por ejemplo en GET puedes usar headers para fingir que eres un navegador web (User-Agent),
mientras que en POST es común usar Content-Type para especificar el formato de los datos que estás enviando."""
