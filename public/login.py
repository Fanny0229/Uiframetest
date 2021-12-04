import time

#创建一个类，类里面的方法可以被调用
class Mylogin(object):
    #Mylogin继承了object类里的方法，object是我们基础的一个类，里面有很多python初始化的一些东西。可以不写，它会默认继承object
    def __init__(self,driver):
        self.driver=driver

    def login(self):
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(2)
        #定位用户名输入框，输入手机号
        self.driver.find_element_by_name('username').send_keys('17778917187')
        #定位密码输入框，输入密码
        self.driver.find_element_by_id('password').send_keys('123qwe')
        #定位登录按钮，点击
        self.driver.find_element_by_class_name('submit_login').click()
        time.sleep(5)