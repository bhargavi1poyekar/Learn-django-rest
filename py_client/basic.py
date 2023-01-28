import requests  # import lib for making requests

endpoint = "http://httpbin.org/"
endpoint="http://httpbin.org/anything"
endpoint="http://localhost:8000/api/rest_post"

# get_response=requests.get(endpoint) # Http request

'''
Http request-> returns HTML
Rest-api http request -> JSON (sometimes XML)

JSON- JavaScript Object Notation
'''



'''
{'args': {}, 'data': '{"query": "Hello"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '18', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.2', 'X-Amzn-Trace-Id': 'Root=1-63d438b4-6d7a232f1b12375720fd6900'}, 'json': {'query': 'Hello'}, 'method': 'GET', 'origin': '69.143.91.132', 'url': 'http://httpbin.org/anything'}
'''
# get_response=requests.get(endpoint,data={"query":"Hello"}) # returns the json data in response as form.

'''
{'args': {}, 'data': '', 'files': {}, 'form': {'query': 'Hello'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '11', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.2', 'X-Amzn-Trace-Id': 'Root=1-63d4398e-295f8e47204483b564c52927'}, 'json': None, 'method': 'GET', 'origin': '69.143.91.132', 'url': 'http://httpbin.org/anything'}
'''

# print(get_response.text) # Raw json response

# get_response=requests.get(endpoint, params={"abc":123},json={"query":"Hello"}) # returns the json data in response as data.

# print(get_response.json()) # Converts the incoming json to python dictionary (Most important=> Null to None)
# print(get_response.text)
# print(get_response.headers)
# print(get_response.status_code) # gives status of response 

'''
POST request
'''

get_response=requests.post(endpoint,json={'content':'Heloo'})

print(get_response.json())








