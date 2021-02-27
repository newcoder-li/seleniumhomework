# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from seleniumpo.page.add_member_page import AddMemberPage


class MainPage:
    # 复用浏览器登录
    def __init__(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def goto_add_member_page(self):
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(1)")
        return AddMemberPage(self.driver)