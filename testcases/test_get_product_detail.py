import allure
import pytest
import requests
from common.common_requests import Requests
from common.tools import get_project_path, sep
from testcases.test_get_search_product import TestId


# class TestApi():
#     @pytest.mark.get_product_detail
#     def test_get_product_detail(self, token):
#         header = {
#             "token": token()
#         }
#         res = Requests(headers=header).post("/api/product/get_product_detail")
#


class TestApi(object):
    @pytest.mark.get_product_detail
    def test_get_product_detail(self, token, get_id):
        id_list = [get_id()]
        print(id_list)
        json = {
            "product_id": 30
        }
        header = {
            "token": token()
        }
        res = Requests(headers=header).post(url = "/api/product/get_product_detail", json=json)
        res_json = res.json()
        print(res.text)
        # print("——" * 50)
        # print(res_json)

        img_url = res_json["data"]["product_detail_image"][0]

        img_bin = requests.get(img_url).content

        load_img_dir = get_project_path() + sep(["img", "autuman.jpeg"], True)
        with open(load_img_dir, "wb") as file_res:
            file_res.write(img_bin)


