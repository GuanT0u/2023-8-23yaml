import pytest
from common.common_requests import Requests
from common.mysql_opreta import MysqlOpreta

class TestApi:
    # 获取钱包信息的接口
    @pytest.mark.get_wallet_info
    def test_get_wallet_info(self, token):
        header = {
            "token": token()
        }
        res = Requests(headers=header).post("/api/wallet/get_wallet_info")
        # print(res.json()["data"["balance"])
        # 写数据验证 这是我作为测试人员自己写的sql验证数据准确性

        data = MysqlOpreta().mysql_query("select balance from wallet where user_id = ")
        
        # 断言  assert  a==b,  "如果a 不等于b 则报出此段话"
        try:
            assert data[0][0] == res.json()["data"]["balance"], ""
        except AttributeError as e:
            print(e)





