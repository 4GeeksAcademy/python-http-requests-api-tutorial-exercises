# `06` Project List

The following endpoint returns a JSON formatted response with several projects in a list:  

GET: [https://assets.breatheco.de/apis/fake/sample/project_list.php](https://assets.breatheco.de/apis/fake/sample/project_list.php)

Each of the projects has the following format (example):

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

1. Please call the endpoint and print the name of the **SECOND** project on the list:

Example output:
```text
Coursera eLearning
```

## 💡 Hints:

+ Open the endpoint on your browser and analyze the response body, you need to know what to expect, what is going to be the structure of the data (response body) coming back from the server.
+ In this case, the response body starts with a square bracket `[`, it's a list, and you have to access the second project by using numerical positions.
+ Make a GET request to the endpoint.
+ Use the [.json() method](https://www.w3schools.com/python/ref_requests_response.asp) to get the response body as a dictionary.
+ Find the second project on the list.
+ Print the project name, you can access the property `name` of the project dictionary.
+ You don't need to loop, just access the second item like a list using the position.

