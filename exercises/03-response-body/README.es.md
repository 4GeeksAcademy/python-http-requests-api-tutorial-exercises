# `03` Response Body

Haga clic en este enlace para ver la respuesta que esta solicitud GET está dando en el body:
[https://assets.breatheco.de/apis/fake/sample/random-status.php](https://assets.breatheco.de/apis/fake/sample/random-status.php)

Ahora, si deseas obtener el *body* de la respuesta (texto/contenido), todo lo que tienes que hacer es:

```py
print(response.text) 
```

## 📝 Instrucciones:

Imprime en la consola el *body* de la respuesta solo para solicitudes con status `200`, para el resto imprime:

```text
"Something went wrong"
```