# -*- coding: utf-8 -*-
import pytest
import yaml
from hamcrest import assert_that

from page.main_page import MainPage

path = "../datas/contract_data.yaml"
with open(path, encoding="utf-8") as f:
    datas: list = yaml.safe_load(f)['datas']
    print(datas)
    for data in datas:
        username = data[0]
        accountname = data[1]
        phone = data[2]


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    @pytest.mark.parametrize('username, accountname, phone', datas)
    def test_add_member(self, username, accountname, phone):
        add_page = self.main.goto_add_member_page()
        add_page.add_member(username, accountname, phone)
        contract_names = add_page.get_member()
        print(contract_names)
        assert username in contract_names
