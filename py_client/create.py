import requests 

endpoint="http://localhost:8000/api/products/"

data={
    'title':'Milk',
}

get_response=requests.post(endpoint, json=data)

print(get_response.json())