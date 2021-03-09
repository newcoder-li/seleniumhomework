# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from seleniumpo.page.add_member_page import AddMemberPage


class MainPage(BasePage):
    # # 复用浏览器登录
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member_page(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        return AddMemberPage(self.driver)