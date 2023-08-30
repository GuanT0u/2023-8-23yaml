import allure
import pytest
from common.common_requests import Requests


json = {
    "default_status": 1,
    "detail_addres": "广东省广州市南沙区榄核镇蔡新路广州新华互联网科技学校",
    "id": 31,  # 尤为重要
    "phone_number": "13855647240",
    "receive_name": "jay"
}



class TestApi():
    @pytest.mark.get_edit_adderss
    def test_get_edit_adderss(self, token):
        with allure.step("登录"):
            header = {
                    "token": token()
                }
        with allure.step("调取用户信息接口"):
            res = Requests(headers=header).post("/api/address/edit_address", json=json)
        with allure.step("打印结果"):
            print(res.text)



