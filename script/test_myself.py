# -*- coding=utf-8 -*-
import time
import os

import pytest

from base import initDriver
from page.page import Page


class TestDemo:

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    # 定义一个 test 函数来对应我们测试用例中执行结果为 “账号不存在” 的那一类用例
    @pytest.mark.parametrize("args", [("18512381234", "123456", "账号不存在!")])
    def test_login_nonum(self,args):

        # 使用 首页模型当中的进入 首页的动作
        self.page.inithomepage.auto_enter_home()
        self.page.inithomepage.click_myself()
        time.sleep(2)  # 涉及到页面转场我们选择停留一定的时间

        # 点击 登录/注册 之前我们需要判断当前是否为登录状态，如果我们则退出
        if self.page.initmyselfpage.is_loging():
            self.page.initmyselfpage.login_out()
            time.sleep(2)
        # 点击登录注册按钮
        self.page.initmyselfpage.click_login_reg()
        time.sleep(1)  # 涉及到页面转场我们选择停留一定的时间

        # 输入账号
        self.page.initmyselfpage.input_num(args[0])

        # 输入密码
        self.page.initmyselfpage.input_pwd(args[1])

        # 点击登录
        self.page.initmyselfpage.click_enter()

        assert_stu = self.page.initmyselfpage.is_toast_exist(args[2])

        if assert_stu:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + 'img\screen.png')

        assert assert_stu

    def test_demo2(self):
        print( "测试代码" )
        assert 0

    def test_demo3(self):
        print( "测试代码" )
        assert 0




