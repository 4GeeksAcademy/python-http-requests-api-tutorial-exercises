# `11` Obtener un archivo adjunto (attachment) por id

# 📝 Instrucciones

Usando el mismo endpoint del ejercicio anterior, crea una función `get_attachment_by_id` que retornes el titulo de los adjuntos que correspondan con el id dado.

## 💡Pista

1. Crea la función `get_attachment_by_id` que reciba el `attachment_id` como un parametro.
2. Recorre (Loop) todos los posts.
3. Recorre (Loop) todos los attachments (adjuntos) de cada post.
4. Si el archivo adjunto (attachment) tiene el `attach_id` dado en el parámetro de la función, devuélvalo.

