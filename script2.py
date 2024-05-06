from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import traceback
from logger import get_logger
from CsvWriter import CSVWriter

class UserDataScrapper:
    def __init__(self,first_name,last_name,id_of_linkdin,_pass):
        """AI is creating summary for __init__

        Args:
            first_name ([Str]): First Name of the user which have been find over the instagram
            last_name ([type]): Last Name of the user which have been find over the instagram
            id_of_linkdin ([str]): Id of the linkdin
            _pass ([str]):pass of the lindin
        """
        try:
            self.driver = webdriver.Chrome()
            self.first_name = first_name
            self.last_name = last_name
            self.id = id_of_linkdin
            self._pass = _pass
            self.login_flag = False
            self.login()
            if self.login_flag:
                self.get_users()
                self.returnProfileInfo()
            else:
                pass
                logger.debug("Login Failed")
        except:
            pass
            logger.error(traceback.format_exc())
        
    def login(self):
        """Using the Cridential login on the linkdin"""
        try:
            self.driver.get("https://www.linkedin.com/login")
            time.sleep(1)
            eml = self.driver.find_element(by=By.ID, value="username")
            eml.send_keys(self.id)
            passwd = self.driver.find_element(by=By.ID, value="password")
            passwd.send_keys(self._pass)
            loginbutton = self.driver.find_element(by=By.XPATH, value="//*[@id=\"organic-div\"]/form/div[3]/button")
            loginbutton.click()
            time.sleep(10)
            self.login_flag = True
        except Exception as e:
            pass
            logger.error(traceback.format_exc())

    def get_users(self):
        """Dcrap the user profile link"""
        try:
            time.sleep(1)
            self.driver.get(f"https://www.linkedin.com/pub/dir/{self.first_name}/{self.last_name}")
            time.sleep(3)
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_data_list = self.driver.find_elements(By.XPATH, "//a[@class='app-aware-link ']")

            user_links = []

            # Iterate through the anchor elements and extract their href attribute
            for user_data in user_data_list:
                user_link = user_data.get_attribute("href")
                if user_link not in user_links:
                     user_links.append(user_link)

            self.user_links = user_links
        except:
            pass
            logger.error(traceback.format_exc)
    

    def returnProfileInfo(self):
        """Scrap the user profile data """
        try:
            list_of_data = set()
            user_data = {}
            for link in self.user_links:
                    self.driver.get(link)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    user_links_list = self.driver.find_elements(By.XPATH, "//img[@id='ember32']")
                    for user_image_link in user_links_list:
                        user_image = user_image_link.get_attribute("src")
                        user_data["Profile Image"] = user_image
                        # print(f"Image{user_image}")
                    titles = self.driver.find_elements(By.XPATH,'//div[@class="text-body-medium break-words"]')
                    for title in titles:
                        Title_text = title.text
                        user_data["title"] = Title_text
                    elements = self.driver.find_elements(By.CLASS_NAME, "display-flex ph5 pv3")
                    user_data["Profile Link"] = link
                    list_of_data.add(user_data)
            CSVWriter(list_of_data)
            # print(list_of_data)
        except:
            pass
            logger.error(traceback.format_exc())
                    
        
if __name__ == "__main__":
    logger = get_logger("log/file.log")
    id_of_linkdin = input("Please enter your linkdin Gmail or Username:   ")
    _pass = input("Please enter password:  ")
    first_name = input("Enter Your First Name:   ")
    last_name = input("Enter Your last Name:   ")
    UserDataScrapper(first_name,last_name,id_of_linkdin,_pass)