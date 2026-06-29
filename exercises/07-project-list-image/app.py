import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

if response.status_code == 200:
    # Parsing JSON response
    project_list = response.json()
    
    # Extracting the last project
    last_project = project_list[-1]
        
    # Extracting the last image URL
    last_image_url = last_project["images"][-1]
            
    # Printing the last image URL
    print(last_image_url)  
else:
    print("Failed to fetch project list.")