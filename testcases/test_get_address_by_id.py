import allure
import pytest
from common.common_requests import Requests


json = {
    "id": 27  # 尤为注意，要有变化; 查看id方法: 设置地址为默认，查看即可
}



class TestApi():
    @pytest.mark.get_address_by_id
    def test_get_address_by_id(self, token):
        with allure.step("登录"):
            header = {
                    "token": token()
                }
        with allure.step("调取用户信息接口"):
            res = Requests(headers=header).post("/api/address/get_address_by_id", json=json)
        with allure.step("打印结果"):
            print(res.text)


