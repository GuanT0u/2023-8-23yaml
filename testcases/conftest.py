import pytest
from common.common_requests import Requests
from common.yaml_config import GetConfig


@pytest.fixture()
def token():
    def _token():
        username, password = GetConfig().get_username_password("jay")
        data = {
            "user": username,
            "password": password
        }
        res = Requests().post("/api/user/login", json=data)
        return res.json()["data"]["token"]
    return _token  # 写完函数时返还函数名字，不要带上括号，带上括号就是一个函数了


# conftest.py 和配置文件差不多
