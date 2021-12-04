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

    def testGouwu01_03(self):
        '''购物车为空时文案是否显示正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//div[@class='small_cart_name']/span").click()
        time.sleep(3)
        emptyGouwuText=self.driver.find_element_by_xpath("//div[@class='r']/span")
        print(emptyGouwuText.text)
        self.assertEqual("购物车内暂时没有商品",emptyGouwuText.text)

if __name__=="__main__":
    unittest.main()