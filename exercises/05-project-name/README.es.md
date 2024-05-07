# `05` Project name

El siguiente endpoint es ideal para recuperar proyectos de estudiantes:

GET [https://assets.breatheco.de/apis/fake/sample/project1.php](https://assets.breatheco.de/apis/fake/sample/project1.php)

```json
{
    "name": "Coursera eLearning",
    "thumb": "https://unsplash.it/450/320?image=178",
    "description": "The coolest eLearning site on the planet",
    "images": [
        "https://unsplash.it/450/320?image=178",
        "https://unsplash.it/450/320?image=179",
        "https://unsplash.it/450/320?image=180",
        "https://unsplash.it/450/320?image=181"
    ]
}
```

## 📝 Instrucciones:

1. Llama al endpoint e imprime el nombre del proyecto en el terminal (solo el nombre del proyecto).

Ejemplo de salida:

```text
Coursera eLearning
```

## 💡 Pistas:

+ Haz una solicitud GET al endpoint.
+ Usa el [metodo .json()](https://www.w3schools.com/python/ref_requests_response.asp) para obtener el response body como un diccionario (igual que en el último ejercicio).
+ Imprime el nombre del proyecto, puedes acceder al nombre de la propiedad en el diccionario de respuestas.

