# import requests

from common.yaml_config import GetConfig

from common.common_requests import Requests

url = GetConfig().get_url()

headers = {
    "token": "JWT eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0cmFkaW5nX3N5c3RlbSIsImlkIjoyMiwiaWF0IjoxNjkyOTI5Mzg3LCJleHAiOjE2OTM1MzQxODd9.PfioygVEwPzlB8N7wWGXrnS4OYxCHXO-YbzYN4_zJWo"
}

# res = requests.post(url + "/api/wallet/get_wallet_info", headers=headers)
# print(res.text)

res = Requests(headers = headers).post("/api/wallet/get_wallet_info")
