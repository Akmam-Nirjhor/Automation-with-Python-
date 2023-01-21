from selenium.webdriver.common.by import By

class confirmPage:
    def __init__(self,driver):
        self.driver = driver

    Box = (By.ID,"country")
    Countryname = (By.LINK_TEXT,"India")
    SquareBox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    PurchaseButton = (By.XPATH,"//input[@type='submit']")

    #driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

    def getBox(self):
        return self.driver.find_element(*confirmPage.Box)

    def getCountry(self):
        return self.driver.find_element(*confirmPage.Countryname)

    def getSquareBox(self):
        return self.driver.find_element(*confirmPage.SquareBox)

    def getPurchase(self):
        return self.driver.find_element(*confirmPage.PurchaseButton)

