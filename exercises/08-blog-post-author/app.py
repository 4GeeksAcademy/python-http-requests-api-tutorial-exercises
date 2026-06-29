import requests

# Your code here
responde = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

if responde.status_code == 200:
    data = responde.json()

    first_post = data['posts'][0]

    author_dic = first_post['author']

    name_author = author_dic['name']

    print(name_author)

else:
    print("Failed to fetch data from the endpoint.")