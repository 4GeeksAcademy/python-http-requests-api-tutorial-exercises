# `04` Response JSON

Pero tener una respuesta basada en texto no es muy útil, es por eso que las API normalmente responden en formato CSV, JSON, YAML o XML.

## 📝 Instrucciones:

El siguiente endpoint devuelve la hora actual en un formato JSON cada vez que se solicita utilizando el método GET.

|    |    |
| ---   | ---   |
| method | GET |
| endpoint | https://assets.breatheco.de/apis/fake/sample/time.php |
| content-type | application/json |

Response body:

```python
{
    "hours": "07",
    "minutes": "29",
    "seconds": "35"
}
```

Haga una solicitud GET a ese endpoint e imprime la hora en la consola con este formato:

```bash
Current time: 17 hrs 06 min and 23 sec
```

## 💡 Pistas:

1. Usa el [metodo .json()](https://www.w3schools.com/python/ref_requests_response.asp) para obtener el response body como un diccionario y almacenarlo en una variable.
2. Obtenga las propiedades `hours`, `minutes` y `seconds` del diccionario.
3. Concatenar todo de esta manera: `Hora actual: 17 h 06 min y 23 seg`.

