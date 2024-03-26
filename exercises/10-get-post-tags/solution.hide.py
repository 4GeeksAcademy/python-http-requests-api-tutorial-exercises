import requests

def get_post_tags(post_id):
    # Your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        # Loop through each post to find the one with matching post_id
        for post in data["posts"]:
            if post["id"] == post_id:
                return post["tags"]
        print("No post found") 

    else:
        print("Failed to fetch data from the endpoint.")


print(get_post_tags(146))