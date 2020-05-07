# `02` Manejar el Status de Respuesta

La siguiente solicitud GET siempre devuelve un código de status diferente, nunca se sabe qué respuesta está recibiendo del servidor.

## 📝Instrucciones

Crea una condición para imprimir en la consola los siguientes mensajes según el status de respuesta:

| Status    | Message   |
| -----     | -----     |
| 404       | The URL you asked is not found |
| 503       | Unavailable right now |
| 200       | Everything went perfect |
| 400       | Something is wrong on the request params |