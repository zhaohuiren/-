#coding=utf-8
import  time
import  unittest
from util.browser import Browser

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

    def test_2yemian(self):
        u"""页面遍历"""
        driver=self.browser
        driver.get('https://wj-01.zleida.com/project/create')
        time.sleep(1)
        title=driver.title
        self.assertEqual(title,"【发布委案】-资产雷达")
        driver.get('https://wj-01.zleida.com/project/index')
       # title=driver.title
        #self.assertEqual(title,"")








def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
