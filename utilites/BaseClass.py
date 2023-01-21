from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import pytest
@pytest.mark.usefixtures("setup")
class BassClass:
    def verifyLinkPresence(self,text):
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))
