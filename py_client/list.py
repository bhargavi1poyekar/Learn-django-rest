import requests 
from getpass import getpass

auth_endpoint="http://localhost:8000/api/auth/"

username=input("Enter username: ")
password=getpass("Enter password: ")

auth_response=requests.post(auth_endpoint,json={"username":username,"password":password})

print(auth_response.json())

if auth_response.status_code==200:
    token=auth_response.json()['token']


    headers={
        "Authorization":f"Token {token}" 
    }

    endpoint="http://localhost:8000/api/products/"

    get_response=requests.get(endpoint, headers=headers)

    print(get_response.json())

    '''
    Pagination
    '''
    # data=get_response.json()
    # results=data['results']
    # print(results)
    
    # should be done recursively
    # next_url=data['next']
    # if next_url is not None:
    #     get_response=requests.get(next_url, headers=headers)
    

