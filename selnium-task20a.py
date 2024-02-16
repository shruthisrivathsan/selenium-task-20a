from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Cowin:
    #initialise a class to take in the url
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    #create a function to load the url and maximise the window
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    #create a function to click on FAQ and open in a new window
    def clickFAQ(self):
        self.boot()
        current_window_handle= self.driver.current_window_handle
        self.driver.find_element(by=By.LINK_TEXT, value="FAQ").click()
        new_window_handle = None
        for window_handle in self.driver.window_handles:
            if window_handle != current_window_handle:
                new_window_handle = window_handle
                break
        if new_window_handle:
            self.driver.switch_to.window(new_window_handle)
        self.closeWindow()

    # create a function to click on partners and open in a new window
    def clickPartners(self):
        self.boot()
        current_window_handle= self.driver.current_window_handle
        self.driver.find_element(by=By.LINK_TEXT, value="Partners").click()
        new_window_handle = None
        for window_handle in self.driver.window_handles:
            if window_handle != current_window_handle:
                new_window_handle = window_handle
                break
        if new_window_handle:
            self.driver.switch_to.window(new_window_handle)
        self.closeWindow()

    #funciton to close the newly opened window
    def closeWindow(self):
        self.driver.close()
        self.driver.switch_to.default_content()

    #create a funciton to exit
    def quit(self):
        self.quit()


url = "https://www.cowin.gov.in/"
obj = Cowin(url)
obj.boot()
obj.clickFAQ()
obj.clickPartners()
obj.quit()