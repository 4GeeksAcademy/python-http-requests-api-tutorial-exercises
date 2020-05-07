# `03` Respuesta en Body

Haga clic en este enlace para ver la respuesta que esta solicitud GET está dando en el body:
[https://assets.breatheco.de/apis/fake/sample/random-status.php](https://assets.breatheco.de/apis/fake/sample/random-status.php)

Ahora, si deseas obtener ese body como respuesta (texto), todo lo que tiene que hacer es:
```py
# plain text
print(response.text) 
```

# 📝 Instrucciones

Imprime en la consola la the responde body solo para solicitudes 200, para el resto imprima "Something went wrong".