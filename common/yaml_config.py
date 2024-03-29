import yaml
from common.tools import get_project_path, sep


class GetConfig():
    def __init__(self):
        # with open("../config/environment.yaml", "r", encoding="utf-8") as env_file:
        with open(get_project_path() + sep(["config", "environment.yaml"], True), "r", encoding='utf-8') as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]

    def get_mysql_config(self):
        return self.env["mysql"]

if __name__ == "__main__":
    print(GetConfig().get_username_password("jay"), GetConfig().get_url())




