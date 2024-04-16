# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNewTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_newTest(self):
    self.driver.get("http://127.0.0.1:5500/")
    self.driver.set_window_size(958, 1031)
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "Select Driver").click()
    self.driver.find_element(By.CSS_SELECTOR, ".car-info-section:nth-child(4) p:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".car-info-section:nth-child(3) p:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".payment-option:nth-child(1) > label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".payment-option:nth-child(2) > label").click()
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
  