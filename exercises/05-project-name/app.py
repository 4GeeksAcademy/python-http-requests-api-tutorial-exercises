import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

if response.status_code == 200:
    # Parsing JSON response
    project_data = response.json()
    
    # Extracting project name
    project_name = project_data["name"]

    print(project_name)
else:
    print("Failed to fetch project data.")