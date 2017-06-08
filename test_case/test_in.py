# utf-8
# test in
import unittest
import time
from util.browser import Browser


class intest(unittest.TestCase):
    def setUp(self):
        # 初始化工作
        self.browser = Browser.BROWSER
        self.verificationErrors = []
        # 定义数组，脚本运行错误记录到这个数组里
        self.accept_next_alert = True
        # 表示接受警告

    def test_1inlogin(self):
        u"""in登录"""
        driver = self.browser
        driver.get("https://ij-01.zleida.com/auth/login")
        driver.find_element_by_name("name").send_keys("admin")
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_id("sub").click()
        time.sleep(2)

    def test_2inxieyi(self):
        u"""in协议"""
        driver = self.browser
        driver.get("https://ij-01.zleida.com/contract/update?contract_id=424")
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(2)
        message = driver.switch_to_alert().text
        time.sleep(2)
        self.assertEqual(message, '协议模板修改成功')
        # 点击弹出框
        driver.switch_to_alert().accept()
        time.sleep(2)
        driver.get("https://ij-01.zleida.com/user/detail?userId=222343")
        driver.get("https://ij-01.zleida.com/user/detail?userId=222343")

        text = driver.find_element_by_xpath(
            "//table[1]//tbody//tr[1]//td[2]").text

        driver.get("https://ij-01.zleida.com/user/detail?userId=222343")

        self.assertEqual(text, "委托测试")

    def test_3inWTdetails(self):
        u"""委托方详情"""
        driver = self.browser
        time.sleep(4)
        driver.get("https://ij-01.zleida.com/contract/detail?ownerId=222343")
        time.sleep(1)
        text = driver.find_element_by_xpath("//tbody//tr[1]//td[2]").text
        time.sleep(1)
        self.assertEqual(text, "信贷")

    # def test_4auto(self):
    #     u"""车委案"""
    #     driver = self.browser
    #     driver.get("https://ij-01.zleida.com/project/manage")
    #     time.sleep(20)
    #     driver.find_element_by_xpath("//li[@id='dlayLi']//a").click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath(
    #         "//table[contains(concat(' ', @class, ' '), ' table-striped ')]//tbody//tr[1]//td[1]//input").click()
    #     drop_down = driver.find_element_by_id("receiverUserId")
    #     drop_down.find_element_by_xpath("//option[@value=222342]").click()
    #     driver.find_element_by_xpath(
    #         "//form[@id='auto-form-seach']//div//div[2]//input[2]").click()
    #     driver.switch_to_alert().accept()
    #     time.sleep(1)
    #     message = driver.switch_to_alert().text
    #     self.assertEqual(message, '操作成功')
    #     time.sleep(1)
    #     driver.switch_to_alert().accept()

    def test_5upweian(self):
        u"""委案上传"""
        driver = self.browser
        driver.get('https://ij-01.zleida.com/manage/upload')
        time.sleep(2)
        driver.find_element_by_name('companyName').send_keys('统计测试')
        driver.find_element_by_name('file').send_keys(
            "E:\\a_测试文件\\委案\\一条.xlsx")
        driver.find_element_by_xpath(
            "//input[contains(concat(' ', @class, ' '), ' btn-default ')]").click()
        time.sleep(3)
        try:
            text = driver.find_element_by_xpath(
                "//div[contains(concat(' ', @class, ' '), ' alert ')]").text
            self.assertEqual(text, '×\n导入成功！')
        except BaseException:
            driver.switch_to_alert().accept()

    def test_6caozuoweian(self):
        u"""信贷委案操作"""
        driver = self.browser
        driver.get("https://ij-01.zleida.com/project/manage")
        driver.find_element_by_xpath("//input[@id='all-select']").click()
        driver.find_element_by_name("collectDays").send_keys('1')
        driver.find_element_by_name("companyName").send_keys('统计处置测试')
        driver.find_element_by_id('btn-pass').click()
        time.sleep(2)
        message = driver.switch_to_alert().text
        self.assertEqual(message, '操作成功')
        driver.switch_to_alert().accept()

    def test_7jibanweian(self):
        u"""急办委案操作"""
        driver = self.browser
        driver.get('https://ij-01.zleida.com/project/todoList')
        driver.find_element_by_id('all-select').click()
        driver.find_element_by_name('collectDays').send_keys('100')
        driver.find_element_by_name('companyName').send_keys('统计处置测试')
        driver.find_element_by_xpath(
            "//div[@id='table-responsive']//div[1]//input[5]").click()
        time.sleep(2)
        message = driver.switch_to_alert().text
        if message == '催收期限不能超过剩余委托期限':
            self.assertEqual(message, '催收期限不能超过剩余委托期限')
            driver.switch_to_alert().accept()
        else:
            self.assertEqual(message, '操作成功')
            driver.switch_to_alert().accept()

    def test_8xinxixiugai(self):
        u"""修改企业信息"""
        driver=self.browser
        driver.get("https://ij-01.zleida.com/user/detail?userId=222549")
        driver.find_element_by_name("updateOperatorjiami-test").click()
        driver.find_element_by_name('updateOperatorConfirmjiami-test').click()
        message=driver.switch_to_alert().text
        self.assertEqual(message,'确定修改吗？')
        driver.switch_to_alert().accept()
        time.sleep(2)
        driver.switch_to_alert().accept()


