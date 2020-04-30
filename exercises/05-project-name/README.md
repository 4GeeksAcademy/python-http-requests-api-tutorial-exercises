# `05` Project name

The following endpoint is ideal to retrieve student projects:  

GET [https://assets.breatheco.de/apis/fake/sample/project1.php](https://assets.breatheco.de/apis/fake/sample/project1.php)

```json
{
    "name": "Coursera eLearning",
    "thumb": "https://unsplash.it/450/320?image=178",
    "description": "The coolest elarning site on the planet",
    "images": [
        "https://unsplash.it/450/320?image=178",
        "https://unsplash.it/450/320?image=179",
        "https://unsplash.it/450/320?image=180",
        "https://unsplash.it/450/320?image=181"
    ]
}
```

# 📝 Instructions

Please call the endpoint and print the project name on the terminal (only the project name)

Example output:
```bash
Coursera eLearning
```

## 💡Hint

1. Similar exercise to the previous one.
2. Do a GET request to the endpoint.
3. Use the [.json() method](https://www.w3schools.com/python/ref_requests_response.asp) to get the response body as a dictionary (same as you did on last exercise).
4. Print the project name, you can access the property name on the response dictionary.

