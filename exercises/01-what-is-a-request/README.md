# 02 What is a request

HTTP is a set of rules that allow two endpoints A - B to communicate with each other in only one direction:
```txt
A = Client     B = Server
```

- The client always asks a `request` to one server URL.
- The server wais for request and answers max one `response` for each request.

In python this is how we make a request:

```python
from http.client import HTTPSConnection

host_url = "assets.breatheco.de"
path = "/apis/fake/hello.php"

conn = HTTPSConnection(host_url)
conn.request("GET", path, body=None, headers={})

r1 = conn.getresponse()
response = {
    "status": r1.status,
    "body": r1.read()
}

print(response)
```

# 📝 Instructions

Change the following code to print on the console `success` if the response status is between 200 and 399 or `fail` if the response is between 400 and 599.

Note: Only print success or fail, do not print anything else.