#coding=utf-8
import  time
import  unittest
from util.browser import Browser
from util.excel import projects

class weituo(unittest.TestCase):
    def setUp(self):
    #初始化工作
        self.browser=Browser.BROWSER
        self.verificationErrors=[]
        #定义数组，脚本运行错误记录到这个数组里
        self.accept_next_alert=True
        #表示接受警告
    def test_1login(self):
         u"""登陆模块"""
         driver=self.browser
         driver.get('https://wj-01.zleida.com/login/login')
         driver.find_element_by_id("name").send_keys("wt-tongji")
         driver.find_element_by_id('password').send_keys('123456')
         driver.find_element_by_xpath("//input[contains(concat(' ', @class, ' '), ' btn ')]").click()
         title=driver.title
         self.assertEqual(title,"【工作平台】-资产雷达")


    def test_2upload(self):
        u"""发布委案"""
        driver=self.browser
        driver.get('https://wj-01.zleida.com/project/create')
        time.sleep(1)
        projects()
        driver.find_element_by_id('file').send_keys(r"E:\a_测试文件\委案导入模板程序.xls")
        driver.find_element_by_id('agreedUpload').click()
        time.sleep(2)
        text=driver.find_element_by_xpath("//div[contains(concat(' ', @class, ' '), ' panel-body ')]//div[1]").text
        self.assertEqual(text,'导入信贷委案成功!')

    def test_3check(self):
        u"""确认催收进度"""
        driver=self.browser
        driver.get('https://wj-01.zleida.com/project/index?status=60')
        driver.find_element_by_xpath("//table[contains(concat(' ', @class, ' '), ' table ')]//tbody//tr[1]//td[3]").click()
        time.sleep(5)
        #取到所有页面的曲柄
        all_handles=driver.window_handles
        #取到当前页面的曲柄
        now_handles=driver.current_window_handle
        # 循环 判断窗口是否为当前窗口
        for handle in all_handles:
            if handle!=now_handles:
        #切换到新窗口
                driver.switch_to_window(handle)
        #取到url
        url=driver.current_url
        #用=截取code
        allurl=url.split('=')
        code=allurl[1]
        print(code)
        #拼接URL
        c="https://wj-01.zleida.com/settlement/settlementOwner?id="+code
        print(c)
        driver.get(c)
        driver.find_element_by_id('yesPass').click()
        time.sleep(2)
        driver.find_element_by_id('receivedAmount').send_keys('100')
        driver.find_element_by_id('yesCommission').click()
        driver.find_element_by_id('submitBtn').click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(concat(' ', @class, ' '), ' yes ')]").click()
        time.sleep(1)
        text=driver.find_element_by_xpath("//div[contains(concat(' ', @class, ' '), ' alert-success ')]//p").text
        self.assertEqual(text,'催收进度审核操作成功！')









def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
