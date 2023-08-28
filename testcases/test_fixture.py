import pytest



class TestFixturl:
    @pytest.fixture()
    def front(self):
        return "htpps://"

    @pytest.mark.bing
    def test_bing(self, front):
         print("bing:",f"{front}cn.bing.com")

    @pytest.mark.baidu
    def test_baidu(self, front):
        print("baidu", f"{front}www.baidu.com")

