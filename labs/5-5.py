import requests
from common.yaml_config import GetConfig

# 先获取yaml配置文件里的账号和密码

username, password = GetConfig().get_username_password("jay")

url = GetConfig().get_url()

data = {
    "user": username,
    "password": password
}

res = requests.post(url + "/api/user/login", json=data)
print(res.text)

