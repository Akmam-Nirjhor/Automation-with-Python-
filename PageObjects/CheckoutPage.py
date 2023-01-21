from selenium.webdriver.common.by import By

class CheckoutPage:


    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR,".card-title a")
    cardFotter= (By.CSS_SELECTOR,".card-footer button")
    checkout = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
    nextChechoutButton = (By.CSS_SELECTOR,".btn.btn-success ")

    def getCardtitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFotter(self):
        return self.driver.find_elements(*CheckoutPage.cardFotter)

    def getChekoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def get2ndChechoutButton(self):
        return self.driver.find_element(*CheckoutPage.nextChechoutButton)







