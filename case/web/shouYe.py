from selenium import webdriver
from public.login import Mylogin
import unittest
import os
import time

class TestShouye(unittest.TestCase):
    '''
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    '''

    def setUp(self):
        #初始化driver，在这里是操作浏览器chrome的一个对象  类后面的参数会传到类的init方法里
        self.driver=webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)
        print('starttime:'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))

    def tearDown(self):
        filedir='C:/1_测试相关/1_作业文件夹/20210919Appium App Ui 自动化测试/screenshot/'
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('C:/1_测试相关/1_作业文件夹/20210919Appium App Ui 自动化测试/screenshot/'))
        print('endtime:'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        screen_name=filedir+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.png'
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        Mylogin(self.driver).login()
        firstPageNavi=self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText=self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText=self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")
        #三个控件定位到了，但核心要实现的是拿到文本信息，和手工用例里的预期进行比对。控件上的文本信息就是实际结果。
        #在unittest框架里会有断言方式

        #assertEqual是断言相等的，预期和实际的断言相等
        self.assertEqual("亲，欢迎来到云商系统商城！",firstPageNavi.text)
        self.assertEqual("17778917187",loginText.text)
        self.assertEqual("退出",regisText.text)
        #对于以上断言，任何一条断言失败了，就不会往下执行了，就抛出报错了

        # #另一种断言方法self.assertNotEqual断言不相等
        # self.assertNotEqual("dd",regisText.text)
        #
        # #第三种self.assertIn 断言前面的内容是否被后面包含
        # self.assertIn("云商系统商城",firstPageNavi.text)
        #
        # #第四种 assertTrue
        # self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())
        #
        # #第五种断言assertFalse
        # self.assertFalse(firstPageNavi.is_displayed())
        #
        # self.assertEqual("True",firstPageNavi.is_displayed())
        #
        # if loginText.text=="17778917187":
        #     print("pass")
        # else:
        #     print("fail")
        # #这样不会报错
        #     self.driver.find_element_by_xpath("wangmazi")
        # #这样在else加一句不可能存在的路径人为搞错，逼他报错


    def testShouye01_02(self):
        '''验证搜索内容无时，提示语是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("wangmazi")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText=self.driver.find_element_by_xpath("//div[@class='nomsg']")
        self.assertEqual(searchText.text,"抱歉，没有找到相关的商品")


if __name__=="__main__":
    unittest.main()






