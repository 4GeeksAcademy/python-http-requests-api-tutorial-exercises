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