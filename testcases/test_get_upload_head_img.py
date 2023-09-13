import pytest
import allure
from common.tools import get_project_path, sep

class TestApi:
    img_list_path = get_project_path() + sep(["img", "R-C.jpg"], True)
    print(img_list_path)

    