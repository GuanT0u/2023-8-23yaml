import pytest
from common.common_requests import Requests
from common.yaml_config import GetConfig

class TestId:
    @pytest.mark.get_search_produc
    def test_get_search_product(self, token):
        json = {
            "product_title": ""
        }
        header = {
            "token": token()
        }
        res = Requests(headers=header).post("/api/product/search_product", json=json)
        print(res.text)
        # print(res.text)
        res_json = res.json()
        # print(res_json)
        data_list = res_json["data"][0:]
        id_url = []
        for x in data_list:
            id_url_ = x["product_id"]
            # print(id_url_)
            id_url.append(id_url_)

        print(id_url)




