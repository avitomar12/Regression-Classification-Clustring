import requests
url='http://127.0.0.1:8080/api'
r=requests.post(url,json={"x":["I love to travel"]})
print(r.json())
