import pytest
from common.common_requests import Requests
from common.yaml_config import GetConfig

class TestApi:
    @pytest.fixture()
    def token(self):
        def _token():
            username, password = GetConfig().get_username_password()
            url = GetConfig().get_url()
            data = {
                "user": username,
                "password": password
            }
            res = Requests().post("/api/user/login", json=data)
            return res.text
        return _token()

    @pytest.mark.get_wallet_info
    def get_wallet_info(self, token):
        header = {
            "token": token()
        }
        res = Requests(headers=header).post("/api/wallet/get_wallet_info")
        print(res.text)
