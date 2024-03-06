"""
using python selenium ,Page object model,pytest, explicit wait, expected condition and chrome driver do Fill the data given in the input Boxes ,select Boxes and drop down menu on the menu and do s search
"""
# own package
from Data import data
from Locatars import locator
from Methods import methods
# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Action Chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.common.keys import Keys
# Exception
from selenium.common.exceptions import NoSuchElementException
import pytest

class TestFillData:
        @pytest.fixture()
        def boot(self):
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get(data.WebData().url)
            self.driver.maximize_window()
            self.action = ActionChains(self.driver)
            for _ in range(9): # using action chains in loop for scroll down the page
                self.action.send_keys(Keys.DOWN).perform()

            yield
            self.driver.quit()
        @pytest.mark.html
        def test_FillData(self, boot):
         """
         This method fill the data in web page input field
         """
         try:
            # name click

            methods.WebMethods().clickButton(self.driver, locator.WebLocators().nameLocator)
            # enter name input field
            methods.WebMethods().enterText(self.driver, locator.WebLocators().nameInputLocator, data.WebData().name)
            # BirthDate click
            for _ in range(5):
                self.action.send_keys(Keys.DOWN).perform()
            methods.WebMethods().clickButton(self.driver, locator.WebLocators().BirthDateLocator)
            # enter text Birth Date input field
            methods.WebMethods().enterText(self.driver, locator.WebLocators().BirthDateInputLocator, data.WebData().BirthDate)
            methods.WebMethods().enterText(self.driver, locator.WebLocators().BirthDateToLocator, data.WebData().ToDate)
            # BirthDay Click
            methods.WebMethods().clickButton(self.driver, locator.WebLocators().BirthDayLocator)
            # enter text Birth day field
            methods.WebMethods().enterText(self.driver, locator.WebLocators().BirthInputDayLocator, data.WebData().BirthDay)

            # see result
            for _ in range(3):
                self.action.send_keys(Keys.DOWN).perform()
            methods.WebMethods().clickButton(self.driver, locator.WebLocators().seeResultButtonLocator)
            # actual url
            actualUrl = self.driver.current_url
            # assert check two strings are equal
            assert actualUrl == data.WebData().dashboardURL
            print("successfully filled")

         except NoSuchElementException as e:
            # element not present in the web page then this block of code execute
             print("Error:Element is not present in the web page")