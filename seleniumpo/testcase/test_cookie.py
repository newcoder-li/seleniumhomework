# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCookie:
    # 初始化driver
    def setup(self):
        # self.main = MainPage()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # get_cookies() 获取当前页面的cookies
        # cookies = self.main.driver.get_cookies()
        # print(cookies)
        # 打开 index页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'hhPAQhmjHdGS2gLRwl7Qwp5_Rq_1Ypz6gL_YEA_c3Xy4o_YdRaAx6Ditr1vPNILYfxdHxgLtwkSVh2zXGd7GHwHiLIkZ5Vn6N8d9lmqTwclPKw4QttusYQlAoO38qHvN1BS_TTEuHCIiKfkegEBmlXHwIp85wksC-BexJJCROrgWyvGTj9xgm3q2xK_VD5ar9HQDVyq-StZ15leEBFt75_2vm22S1POciNee49dt_IJfUUu9-NJPX2u9D0X9e_3s1y2Z4PO9WctJUaQXSDhmrg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850004594449'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325120423784'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '-ip0RAeUuf5ILgM01tvkzg1T6QYUKRDWTcOPZYS1CCHxu0i3XNw5dnQtihfKWnyI'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9736984'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645953877, 'httpOnly': False,
                                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                    'value': '1614343152,1614343385,1614415335,1614417878'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '41249497871476670'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1614417938, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1614446870, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '44ce16s'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1617009928, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1614504298, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.618316436.1614270993'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '526843078'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1614417878'},
            {'domain': '.qq.com', 'expiry': 1677489898, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1103876214.1613886576'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850004594449'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1645422571, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_upload_contact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'hhPAQhmjHdGS2gLRwl7Qwp5_Rq_1Ypz6gL_YEA_c3Xy4o_YdRaAx6Ditr1vPNILYfxdHxgLtwkSVh2zXGd7GHwHiLIkZ5Vn6N8d9lmqTwclPKw4QttusYQlAoO38qHvN1BS_TTEuHCIiKfkegEBmlXHwIp85wksC-BexJJCROrgWyvGTj9xgm3q2xK_VD5ar9HQDVyq-StZ15leEBFt75_2vm22S1POciNee49dt_IJfUUu9-NJPX2u9D0X9e_3s1y2Z4PO9WctJUaQXSDhmrg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850004594449'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325120423784'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '-ip0RAeUuf5ILgM01tvkzg1T6QYUKRDWTcOPZYS1CCHxu0i3XNw5dnQtihfKWnyI'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9736984'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645953877, 'httpOnly': False,
                                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                    'value': '1614343152,1614343385,1614415335,1614417878'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '41249497871476670'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1614417938, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1614446870, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '44ce16s'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1617009928, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1614504298, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.618316436.1614270993'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '526843078'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1614417878'},
            {'domain': '.qq.com', 'expiry': 1677489898, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1103876214.1613886576'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850004594449'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1645422571, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, './/*[@id="js_upload_file_input"]').send_keys("D:\通讯录批量导入模板.xlsx")
        self.driver.implicitly_wait(3)
        assert "通讯录批量导入模板.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text
        self.driver.find_element(By.ID, "submit_csv").click()
        self.driver.implicitly_wait(5)
        assert self.driver.find_element(By.ID, "reloadContact").is_enabled()

    #     # 实现 cookie 数据的持久化存储
    #
    # def test_shelve(self):
    #     # shelve python 内置的模块，相当于小型的数据库
    #     # 带有登录信息的cookie
    #     db = shelve.open('./mydbs/cookies')
    #     # db['cookie'] = cookies
    #     # db.close()
    #     cookies = db['cookie']
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     for cookie in cookies:
    #         if 'expiry' in cookie.keys():
    #             cookie.pop("expiry")
    #         self.driver.add_cookie(cookie)
    #
    #     # 重新打开 已带有cookie 信息的index 页面
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #
    #     self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
    #     self.driver.find_element(By.ID, "js_upload_file_input").send_keys("/Users/juanxu/Downloads/mydata.xlsx")
    #     assert "mydata.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text
