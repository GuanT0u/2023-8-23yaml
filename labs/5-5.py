import requests
from common.yaml_config import GetConfig

username, password = GetConfig().get_username_password()

url = GetConfig().get_url()

data = {
    "user": username,
    "password": password
}

res = requests.post(url + "/api/user/login", json=data)
print(res.text)

