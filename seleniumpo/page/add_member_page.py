# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self, username, accountname, phone):
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(accountname)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        '''
        获取所有联系人姓名
        :return:
        '''
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")))
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.wait_for_click(10, locator)
        while self.driver.find_element_by_css_selector(".ww_commonImg ww_commonImg_PageNavArrowRightNormal").is_enabled():
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            names = []
            for ele in elements:
                names.append(ele.get_attribute("title"))
            return names