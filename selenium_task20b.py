from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
class LabourGov:
    #initialise a class to take in the url
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    #create a function to load the url and maximise the window
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    #create a sleep function
    def sleep(self,secs):
        self.sleep(secs)
    #create a function to move over to "Documents"
    def moveOverDocuments(self):
        document = self.driver.find_element(By.NAME, "Documents")
        self.action.move_to_element(document).perform()
        self.sleep(5)

    #create a function to click on the "download reports"
    def downloadReport(self):
        self.moveOverDocuments()
        xpath = "/html/body/nav/div/div/div/ul/li[7]/ul/li[2]/a"
        return self.driver.find_element(by=By.XPATH, value=xpath).click()

    #create a funciton to exit
    def quit(self):
        self.quit()


url = "https://labour.gov.in/"
obj = LabourGov(url)
obj.boot()
obj.downloadReport()
obj.quit()