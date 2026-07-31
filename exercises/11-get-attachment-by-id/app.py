import requests

def get_attachment_by_id(attachment_id):
    # Your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        for post in data["posts"]:
            # Check if the post has attachments
            if "attachments" in post:
                # Loop through each attachment
                for attachment in post["attachments"]:
                    if attachment["id"] == attachment_id:
                        return attachment["title"]
        
        print("No attachment found")
    else:
        print("Failed to fetch data from the endpoint.")

print(get_attachment_by_id(137))