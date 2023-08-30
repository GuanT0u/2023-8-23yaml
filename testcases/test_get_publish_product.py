import allure
import pytest
from common.common_requests import Requests

json = {
    "product_title": "123",
    "product_desc": "234",
    "product_stock": 1,
    "product_img": ["https://ts1.cn.mm.bing.net/th/id/R-C.b7a22036daf2461b2b71dda797da8a8a?rik=OvQYAf4FjhlKSA&riu=http%3a%2f%2fupload.gogouai.com%2f2019%2f07%2f1563846638zMYRjQ.jpg&ehk=UBfHK4HQNAh9tuOQVcVlsRKmAkQHwwAjzz8OvvH1lWw%3d&risl=&pid=ImgRaw&r=0"],
    "product_price": 345,
    "product_status": 1
 }

class TestApi():
    @pytest.mark.get_publish_product
    def test_get_publish_product(self, token):
        with allure.step("登录"):
            header = {
                "token": token()
            }
        with allure.step("调取用户信息接口"):
            res = Requests(headers=header).post("/api/product/publish_product", json=json)
        with allure.step("打印结果"):
            print(res.text)

