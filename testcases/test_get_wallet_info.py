import pytest
from common.common_requests import Requests
from common.yaml_config import GetConfig

class TestApi:
    # 获取钱包信息的接口
    @pytest.mark.get_wallet_info
    def test_get_wallet_info(self, token):
        header = {
            "token": token()
        }
        res = Requests(headers=header).post("/api/wallet/get_wallet_info")
        print(res.text)




