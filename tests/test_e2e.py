from selenium import webdriver
import time
import pytest
import time
from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import confirmPage
from PageObjects.HomePage import HomePage
from utilites.BaseClass import BassClass


# self.verifyLinkPresence("inida")


class  TestOne(BassClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutPage= CheckoutPage(self.driver)
        cards = checkoutPage.getCardtitles()
        ConfirmPage = confirmPage(self.driver)



        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)

            if cardText == "Blackberry":
                checkoutPage.getCardFotter()[i].click()

        checkoutPage.getChekoutbutton().click()
        checkoutPage.get2ndChechoutButton().click()








