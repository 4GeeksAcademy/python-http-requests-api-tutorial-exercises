# `04` Response JSON

But having a text based response is not very useful, that is why APIs normally respond in CSV, JSON, YAML or XML format.

## 📝 Instructions:

The following endpoint returns the current time in a JSON format every time it is requested using the GET method.

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

1. Please do a GET request to that endpoint and print the time on the console with this format:

```text
Current time: 17 hrs 06 min and 23 sec
```

## 💡 Hints:

+ Use the [.json() method](https://www.w3schools.com/python/ref_requests_response.asp) to get the response body as a dictionary and store it in a variable.
+ Get the `hours`, `minutes` and `seconds` properties from the dictionary.
+ Concatenate everything together like this: `Current time: 17 hrs 06 min and 23 sec`.

