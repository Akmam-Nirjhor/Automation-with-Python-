from selenium.webdriver.common.by import By
import pytest
class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME,"name")
    Email = (By.XPATH,"//input[@class='form-control ng-untouched ng-pristine ng-invalid']")
    Paswword = (By.XPATH,"//input[@type='password']")
    clickBox = (By.XPATH,"//input[@type='checkbox']")
    EmployStatus = (By.XPATH,"//input[@value='option1']")
    Gender = (By.XPATH,"//select[@class='form-control']")
    Female = (By.XPATH,"//select[@class='form-control']/option[2]")


    shop = (By.CSS_SELECTOR,"a[href*='shop']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getMail(self):
        return self.driver.find_element(*HomePage.Email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.Paswword)


    def getclickBox(self):
        return self.driver.find_element(*HomePage.clickBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.Gender)

    def getMale(self):
        return self.driver.find_element(*HomePage.Female)

    def getEmployStatus(self):
        return self.driver.find_element(*HomePage.EmployStatus)


