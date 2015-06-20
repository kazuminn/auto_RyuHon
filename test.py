#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# プロジェクトのパッケージを sys.path に追加する
sys.path.append('django.contrib.auth')

import os
# 環境変数 DJANGO_SETTINGS_MODULE にプロジェクトの settings をセット
os.environ['DJANGO_SETTINGS_MODULE'] = 'tosyokan.settings'

# Model モジュールをインポートする
from django.contrib.auth.models import User

# データベースを操作可能になる


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

for one_user in User.objects.filter(username__contains=""):
    username = one_user.username
    password = one_user.first_name
    
    class Sel(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.PhantomJS()
            self.driver.implicitly_wait(30)
            self.base_url = "https://opac.lib.u-ryukyu.ac.jp/"
            self.verificationErrors = []
            self.accept_next_alert = True
        
        def test_sel(self):
            driver = self.driver
            driver.get(self.base_url + "/cgi-bin/portallogin.cgi?plang=jpn")
            driver.find_element_by_css_selector("input.button").click()
            driver.find_element_by_id("username").send_keys(username)
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_css_selector("input[type=\"submit\"]").click()
            driver.find_element_by_link_text(u"確認する").click()
#            driver.find_element_by_id("lending_line").click()
            
            numbook = 1
        
            while numbook > 10:
                
                try:
                    driver.find_element_by_name("lending_line" + numbook).click()
                    driver.find_element_by_css_selector("input[type=\"button\"]").click()
                except:
                   continue 
                numbook = numbook + 1
                
                
        def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException, e: return False
            return True
        
        def is_alert_present(self):
            try: self.driver.switch_to_alert()
            except NoAlertPresentException, e: return False
            return True
        
        def close_alert_and_get_its_text(self):
            try:
                alert = self.driver.switch_to_alert()
                alert_text = alert.text
                if self.accept_next_alert:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            finally: self.accept_next_alert = True
        
        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

    suite = unittest.TestLoader().loadTestsFromTestCase(Sel)
    len(unittest.TextTestRunner(verbosity=2).run(suite).errors) 
#        send_mail('django_test', 'this is area to display user_id and buying item', 'e145702@ie.u-ryukyu.ac.jp', ['e145702@ie.u-ryukyu.ac.jp'], fail_silently=False)
       

