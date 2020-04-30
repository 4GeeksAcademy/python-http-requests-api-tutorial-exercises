# `06` Project List

The following endpoint returns a JSON formated response with several projects in a list:  

GET: [https://assets.breatheco.de/apis/fake/sample/project_list.php](https://assets.breatheco.de/apis/fake/sample/project_list.php)

Each of the projects has the following format (example):
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

Please call the endpoint and print the name of the **SECOND** project on the list:

Example output:
```bash
Coursera eLearning
```

## 💡Hint

1. Open the endpoint on your browser and analyze the response body, you need to know what to expect, what is going to be the structure of the data (response body) coming back from the server.
2. In this case the response body starts with a square bracket `[`, it's a list, you have to access the second project by using numerical positions.
2. Do a GET request to the endpoint.
3. Use the [.json() method](https://www.w3schools.com/python/ref_requests_response.asp) to get the response body as a dictionary.
4. Find the second project on the list.
5. Print the project name, you can access the property name of the project dictionary.
6. You don't need to loop, just access the second item like a list using the position

