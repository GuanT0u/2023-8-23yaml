import pytest
from common.common_requests import Requests
from common.yaml_config import GetConfig

class TestApi:
    @pytest.fixture()
    def token(self):
        def _token():
            username, password = GetConfig().get_username_password("jay")
            url = GetConfig().get_url()
            data = {
                "user": username,
                "password": password
            }
            res = Requests().post("/api/user/login", json=data)
            return res.json()["data"]["token"]
        return _token  # 写完函数时返还函数名字，不要带上括号，带上括号就是一个函数了

    # 获取钱包信息的接口
    @pytest.mark.get_wallet_info
    def test_get_wallet_info(self, token):
        header = {
            "token": token()
        }
        res = Requests(headers=header).post("/api/wallet/get_wallet_info")
        print(res.text)
