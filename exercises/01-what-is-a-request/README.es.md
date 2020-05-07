# 02 Creando una solicitud (request)

Python tiene un [paquete de solicitud (requests package)](https://requests.readthedocs.io/en/master/) eso permite a los desarrolladores crear solicitudes HTTP con bastante facilidad.

Así es como en Python hacemos una solicitud HTTP GET:

```python
response = requests.get('<destination url>')
print(response.status_code)
```

# 📝 Instrucciones

Cambie la variable URL para que solicite:

```bash
https://assets.breatheco.de/apis/fake/sample/hello.php
```

Nota: La consola debe imprimir un código de estado 200.