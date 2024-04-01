# 01 Creating a request

Python has a [requests package](https://requests.readthedocs.io/en/master/) that allows developers to create HTTP request pretty easily.

In python this is how we make an HTTP GET request:

```python
response = requests.get('<destination url>')
print(response.status_code)
```

# 📝 Instructions

Change the variable url to make it request to: 

```bash
https://assets.breatheco.de/apis/fake/sample/hello.php
```

Note: The console should print a 200 status code.