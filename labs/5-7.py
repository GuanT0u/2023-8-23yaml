from common.yaml_config import GetConfig
from common.common_requests import Requests

url = GetConfig().get_url()

token = "JWT eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0cmFkaW5nX3N5c3RlbSIsImlkIjoyMiwiaWF0IjoxNjkyODYzMjI4LCJleHAiOjE2OTM0NjgwMjh9.7icPSeTJCpI1xfdMcGOBSFYm8nHwF9cZHIO-n4L-7ME"


header = {
    "token": token
}

# res = requests.get(url + "/api/router/router_list/", headers=header)
# print(res.text)

# res = Requests(url + "/api/router/router_list/", headers=header)
# print(res.text)

res = Requests(headers=header).get("/api/router/router_list/")
print(res.text)

