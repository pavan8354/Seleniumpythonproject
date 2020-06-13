

import pytest
from selenium import webdriver

class Testsample():


    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(
            executable_path="C:/Users/Dell/PycharmProjects/new project/Sampleprojects/Drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self, test_setup):
        driver.get("http://opensource-demo.orangehrmlive.com/index.php/auth/login")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

        x = driver.title
        assert x == "OrangeHRM"

