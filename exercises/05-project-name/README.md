# `05` Project name

The following endpoint is ideal to retrieve student projects:  

GET [https://assets.breatheco.de/apis/fake/sample/project1.php](https://assets.breatheco.de/apis/fake/sample/project1.php)

```json
{
    "name": "Coursera eLearning",
    "thumb": "https://unsplash.it/450/320?image=178",
    "description": "The coolest eLearning site on the planet",
    "images": [
        "https://unsplash.it/450/320?image=178",
        "https://unsplash.it/450/320?image=179",
        "https://unsplash.it/450/320?image=180",
        "https://unsplash.it/450/320?image=181"
    ]
}
```

## 📝 Instructions:

1. Please call the endpoint and print the project name on the terminal (only the project name).

Example output:

```text
Coursera eLearning
```

## 💡 Hints:

+ Make a GET request to the endpoint.
+ Use the [.json() method](https://www.w3schools.com/python/ref_requests_response.asp) to get the response body as a dictionary (same as you did on the last exercise).
+ Print the project name; you can access the property name in the response dictionary.

