# `05` Nombre de Proyecto

El siguiente endpoint es ideal para recuperar proyectos de estudiantes:

GET [https://assets.breatheco.de/apis/fake/sample/project1.php](https://assets.breatheco.de/apis/fake/sample/project1.php)

```json
{
    "name": "Coursera eLearning",
    "thumb": "https://unsplash.it/450/320?image=178",
    "description": "The coolest elarning site on the planet",
    "images": [
        "https://unsplash.it/450/320?image=178",
        "https://unsplash.it/450/320?image=179",
        "https://unsplash.it/450/320?image=180",
        "https://unsplash.it/450/320?image=181"
    ]
}
```

# 📝 Instrucciones

Llama al endpoint e imprime el nombre del proyecto en el terminal (solo el nombre del proyecto)

Example output:
```bash
Coursera eLearning
```

## 💡Pista

1. Ejercicio similar al anterior.
2. Haz una solicitud GET al endpoint.
3. Usa el [metodo .json()](https://www.w3schools.com/python/ref_requests_response.asp) para obtener el response body como un diccionario (igual que lo hizo en el último ejercicio).
4. Imprime el nombre del proyecto, puedes acceder al nombre de la propiedad en el diccionario de respuestas.

