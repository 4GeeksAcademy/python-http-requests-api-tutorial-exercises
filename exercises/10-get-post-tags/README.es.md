---
tutorial: "https://www.youtube.com/watch?v=l9e-lSsYNOI"
---

# `10` Get post tags

## 📝 Instrucciones:

1. Usando el mismo endpoint del ejercicio anterior, crea una función `get_post_tags` que retorne el arreglo de etiquetas (tags) de un `post_id` dado.

## 💡 Pistas:

+ Crea la función `get_post_tags`.
+ Obtén todas las publicaciones (post) haciendo la solicitud GET al endpoint.
+ Declare la variable para almacenar el body serializado.
+ Usando el parámetro `post_id`, recorre con un loop todas las publicaciones y compara sus ID para ver si coinciden con el `post_id`.
+ Cuando encuentres la publicación que deseas, devuelve una lista de etiquetas (tags).

