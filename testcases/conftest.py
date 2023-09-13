import pytest
import os
import json
from common.common_requests import Requests
from common.login import login
from common.tools import sep, get_project_path



@pytest.fixture()
def token():
    def _token():
        user = "jay"
        # 老的请求方法，每次请求都需要消耗资源请求token。
        # username, password = GetConfig().get_username_password("jay")
        # data = {
        #     "user": username,
        #     "password": password
        # }
        # res = Requests().post("/api/user/login", json=data)

        # 新的请求方法，封装一个login模块调用现成token，好处是不用经常消耗资源。
        # 第一步: 判断有无存放token文件的文件夹(目录), 有: 就直接读取文件夹下面的文件 没有: 就创建
        token_dir = sep([get_project_path(), "token_dir"])  # 拼接token目录的地址

        # ”os.path.exists“ 的意思是检查指定路径是否存在，在这里是查找token_dir存不存在
        # if os.path.exists(token_dir):
        #     pass
        # else:
        # os.mkdir(token_dir)
        if not os.path.exists(token_dir):  # 判断token_dir不存在
            # os.mkdir 用于创建一个新的目录(文件夹)
            os.mkdir(token_dir)

        # 第二步: 读取token_dir文件夹下面的token文件, 有: 读取文件 没有: 创建json文件，同时你要调取login接口写文件
        # 和上面的一样，判断是否存在
        token_json = sep([token_dir, "token.json"])  # 拼接token.json
        if not os.path.exists(token_json):  # 判断token_json 不存在
            print(f"{user}对应的token文件不存在, 然后调取login模块获取token")
            # 调取login函数并将获取token并写入
            token = login().json()["data"]["token"]
            # 写入token至token_json文件
            with open(token_json, "w") as token_file:  # 创建token_file文件, "w"写入模式至token_file
                print(f"{user}将这个获取到的token字符存储到token.json里")
                # ”<文件>.write(json.dumps(<文件>))“ 是将JSON对象转换为字符串形式，并将该字符串写入文件
                token_file.write(json.dumps(token))
            return token
        else:
            print(f"{user}对应的token文件存在，直接读取")
            with open(token_json, "r") as token_file:
                token = json.loads(token_file.read())
                return token
        # 第三步:

        # return login().json()["data"]["token"]
    return _token  # 写完函数时返还函数名字，不要带上括号，带上括号就是一个函数了

@pytest.fixture()
def get_id(token):  # 获取id
    def _get_id():
        # 传参
        json = {
            "product_title": ""
        }
        header = {
            "token": token()
        }
        res = Requests(headers=header).post("/api/product/search_product", json=json)
        # print(res.text)
        res_json = res.json()
        # print(res_json)
        data_list = res_json["data"][0:]
        id_url = []
        for x in data_list:
            id_url_ = x["product_title"], x["product_id"]  # 循环出来
            id_url.append(id_url_)  # 放到id_url这个列表里

        return id_url

    return _get_id


# conftest.py 和配置文件差不多


