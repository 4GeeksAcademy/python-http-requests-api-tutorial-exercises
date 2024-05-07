# `02` Handle Response Status

The following GET request is always returning a different status code; you never know what response you are getting from the server.

## 📝 Instructions:

Create a condition to print on the console the following messages, depending on the response status:

| Status    | Message   |
| -----     | -----     |
| 404       | The URL you asked for is not found |
| 503       | Unavailable right now |
| 200       | Everything went perfect |
| 400       | Something is wrong with the request params |
| Any other code | Unknown status code |