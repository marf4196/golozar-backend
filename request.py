import requests

login = requests.post("http://127.0.0.1:8000/login/", data={'username': 'admin', 'password': 'admin'})
print('LOGIN: ',login.status_code, login.reason)

# login = requests.post("http://127.0.0.1:8000/login/", data={'username': 'admin', 'password': 'admin'})
# print('LOGIN: ',login.status_code, login.reason)

# login = requests.post("http://127.0.0.1:8000/login/", data={'username': 'admin', 'password': 'admin'})
# print('LOGIN: ',login.status_code, login.reason)