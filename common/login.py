from common.yaml_config import GetConfig
from common.common_requests import Requests

def login():
    username, password = GetConfig().get_username_password("jay")
    data = {
        "user": username,
        "password": password
    }

    res = Requests().post("/api/user/login", json=data)
    return res


if __name__ == "__main__":
    print(login().text)


