import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

if response.status_code == 200:
    # Parsing JSON response
    project_list = response.json()
    
    # Extracting the name of the second project
    second_project_name = project_list[1]["name"]
        
    print(second_project_name)
else:
    print("Failed to fetch project list.")