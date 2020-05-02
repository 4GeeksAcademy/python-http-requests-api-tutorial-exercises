# `10` Obtener etiqueta de publicación

# 📝 Instrucciones

Usando el mismo endpoint del ejercicio anterior, crea una función `get_post_tags` que retorne el arreglo de etiquetas (tags) de un `post id` dado.

## 💡Pista

1. Crea la función `get_post_tags`.
2. Obtén todas las publicaciones (post) haciendo la solicitud GET al endpoint.
3. Declare la variable para almacenar el body serializado 
4. Usando el parámetro `post_id`, recorre con un loop todas las publicaciones y compara sus ID para ver si coinciden con el` post_id`.
3. Cuando encuentres la publicación que deseas, devuelve una lista de etiquetas (tags)

