import requests

def get_titles():
    # Your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    
    titles = []
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        for post in data["posts"]:
            title = post["title"]
            if title:
                titles.append(title)
    else:
        print("Failed to fetch data from the endpoint.")

    return titles


print(get_titles())