# `06` Lista de Proyectos

El siguiente endpoint devuelve una respuesta con formato JSON con varios proyectos en una lista:  

GET: [https://assets.breatheco.de/apis/fake/sample/project_list.php](https://assets.breatheco.de/apis/fake/sample/project_list.php)

Cada uno de los proyectos tiene el siguiente formato (ejemplo):
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

Llame al punto final e imprima el nombre del **SEGUNDO** proyecto en la lista:

Ejemplo:
```bash
Coursera eLearning
```

## 💡Pista

1. Abre el endpoint en tu navegador y analiza la respuesta que se encuentra en el body, necesitas saber qué esperar, cuál será la estructura de los datos (body response) que regresan del servidor.
2. En este caso, el body response comienza con un corchete `[`, es una lista, debe acceder al segundo proyecto utilizando posiciones numéricas.
2. Haga una solicitud GET al endpoint.
3. Usa el [metodo .json()](https://www.w3schools.com/python/ref_requests_response.asp)para obtener el body response como un diccionario.
4. Encuentra el segundo proyecto
5. Imprime el nombre del proyecto, puedes acceder a la propiedad nombre "name" del diccionario del proyecto.
6. No necesitas hacer un bucle (loop), solo accede al segundo elemento como una lista usando la posición

