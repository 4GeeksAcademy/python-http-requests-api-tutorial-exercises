---
tutorial: "https://www.youtube.com/watch?v=S2qXbTLRyGA"
---

# `06` Project List

El siguiente endpoint devuelve una respuesta en formato JSON con varios proyectos en una lista:  

GET: [https://assets.breatheco.de/apis/fake/sample/project_list.php](https://assets.breatheco.de/apis/fake/sample/project_list.php)

Cada uno de los proyectos tiene el siguiente formato (ejemplo):

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

1. Llama al endpoint e imprime el nombre del **SEGUNDO** proyecto en la lista:

Ejemplo de salida:

```text
Coursera eLearning
```

## 💡 Pistas:

+ Abre el endpoint en tu navegador y analiza la respuesta que se encuentra en el body, necesitas saber qué esperar, cuál será la estructura de los datos (response body) que devuelve el servidor.
+ En este caso, el response body comienza con un corchete `[`, es una lista, debes acceder al segundo proyecto utilizando posiciones numéricas.
+ Haz una solicitud GET al endpoint.
+ Usa el [metodo .json()](https://www.w3schools.com/python/ref_requests_response.asp) para obtener el response body como un diccionario.
+ Encuentra el segundo proyecto de la lista.
+ Imprime el nombre del proyecto, puedes acceder a la propiedad `name` del diccionario del proyecto.
+ No necesitas hacer un bucle (loop), solo accede al segundo elemento como una lista usando la posición.

