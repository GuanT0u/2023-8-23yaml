import allure
import pytest
from common.common_requests import Requests


json = {
    "id": 39  # 尤为注意 要有变化; 查看id方法: 设置地址为默认，查看即可
}



class TestApi():
    @pytest.mark.get_delete_adderss
    def test_get_delete_adderss(self, token):
        with allure.step("登录"):
            header = {
                    "token": token()
                }
        with allure.step("调取用户信息接口"):
            res = Requests(headers=header).post("/api/address/delete_address", json=json)
        with allure.step("打印结果"):
            print(res.text)
