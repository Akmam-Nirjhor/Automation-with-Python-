import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilites.BaseClass import BassClass
from PageObjects.HomePage import HomePage
import pytest



class TestHomepage(BassClass):
    def test_fromsubmittion(self,getdata):
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getdata[1])
        homepage.getMail().send_keys(getdata[3])
        homepage.getPassword().send_keys(getdata[4])
        homepage.getclickBox().click()
        homepage.getGender().click()
        homepage.getMale().click()
        homepage.getEmployStatus().click()

    @pytest.fixture(params = [("Akmam","Nirjhor","Male","akmamnirjhor47@gmail.com","2030514.js@1")])
    def getdata(self, request):
        return request.param