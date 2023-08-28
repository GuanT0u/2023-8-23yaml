import requests
from requests.adapters import HTTPAdapter
from common.yaml_config import GetConfig

class Requests:
    def __init__(self, headers, timeout=10):
        """
        requests封装
        Args:
            timeout: 每个请求的超时时间
        """
        self.s = requests.Session()  # 它可以自动处理cookies，做状态保持。用对象属性把原来的requests模块的
        # 在Session实例上挂载Adapter实例，目的：请求异常时，自动重试
        self.s.mount = ("http://", HTTPAdapter(max_retries=3))
        self.s.mount = ("https://", HTTPAdapter(max_retries=3))

        # 公共的请求头设置
        self.s.headers = headers  # .s: 从self.s = re.s继承过来的
        self.timeout = timeout  # 自己定义的属性
        self.url = GetConfig().get_url()  # 自己定义的属性

    def __del__(self):
        """
        当实例被销毁时，释放掉Session所持的所有连接
        :return:
        """
        if self.s:
            self.s.close()


    # 设置get请求
    def get(self, url, params=None):
        """
        GET
        Args:
            url: 接口地址
            param: 一般GET的参数都是放在URL查询参数里面

        :return:

        """
        res = self.s.get(self.url + url, params=params, timeout=self.timeout)
        return res


    # 设置POST请求
    def post(self, url, data=None, json=None):
        """
        POST
        Args:
            url: 接口地址
            data: 参数放在表单参数中
            json: 参数放在请求体中(这时候 Content-Type: opplication/json"内容-类型: 应用程序/JSON")

        :return:

        """
        if data:
            res = self.s.post(self.url + url, data=data, timeout=self.timeout)
            return res
        if json:
            res = self.s.post(self.url + url, json=json, timeout=self.timeout)
            return res
        res = self.s.post(self.url + url, timeout=self.timeout)
        return res



