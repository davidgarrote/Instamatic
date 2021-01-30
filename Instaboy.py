from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

        """Loading Instagram Web"""

        print("Loading Instagram...")
        self.driver.get("https://instagram.com")
        sleep(2)

        """Accepting cookies"""

        print("Accepting cookies...")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        sleep(2)

        """Login"""

        print("Logging you in...")
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        print("You have been logged in!")
        sleep(5)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not now')]").click()
            sleep(2)
        except:
            sleep(1)
        print("Successfully declined notifications...")


    """Defining the function to find, like, comment and follow"""

    def find_posts(self, comment1):

        """Creating variables to keep count of amount of likes, comments and follows"""
        likes = 0
        comments = 0
        follows = 0

        while True:

            try:
                print("Alright time to find some posts!")
                self.driver.get("https://instagram.com/explore/tags/YOURSEARCHKEYWORD/")
                sleep(3)
            except:
                pass

            try:
                """Find post"""


                while self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]") is None:
                    while not self.driver.get("https://instagram.com/explore/tags/YOURSEARCHKEYWORD/"):
                        sleep(10)
                        self.driver.get("https://instagram.com/explore/tags/YOURSEARCHKEYWORD/")
                        sleep(5)
                    self.driver.get("https://instagram.com/explore/tags/YOURSEARCHKEYWORD/")

                self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]").click()
                print(f" Opened latest post!")

                sleep(10)
            except:
                pass

            try:
                """Like post"""

                print("Trying to like the post...")
                self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
                sleep(6)
                print("Post liked succesfully!")
                likes +=1
                sleep(2)
            except:
                pass

            try:
                """Comment post"""

                print("Trying to leave a comment...")
                commentarea = self.driver.find_element_by_class_name('Ypffh')
                commentarea.click()
                sleep(5)
                commentarea = self.driver.find_element_by_class_name('Ypffh')
                commentarea.click()
                sleep(5)
                self.comment1 = comment1
                commentarea.send_keys(comment1)
                sleep(6)
                self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]").click()
                print("Comment left successfully!")
                comments += 1
                sleep(5)
            except:
                pass
            try:
                """Open user profile"""

                print("Opening user profile...")
                if self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a") is None:
                    pass
                else:
                    self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").click()
                    sleep(10)
                if self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]") is not None:
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
                    print("User followed! Remember to unfollow them later.")
                    follows += 1
                    print(f"{likes} likes, {comments} comments and {follows} follows so far")
                    print("I am tired! Sleeping for 2 minutes zZzZzZ")
            except:
                pass

                """Make sure user has been followed"""
            try:
                if self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]") is not None:
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
                    print("User followed! Remember to unfollow them later.")
                    follows += 1
                    print(f"{likes} likes, {comments} comments and {follows} follows so far")
                    print("I am tired! Sleeping for 2 minutes zZzZzZ")

                    sleep(120)
                else:
                    print("User wasn't followed, something happened.")
                    print("Sleeping for 2 minutes zZzZzZ")
                    sleep(120)
            except:
                pass
            sleep(240)


"""Remember to edit this section and the rest on capital letters"""

my_bot = Instabot('YOURUSERNAME', 'YOURPASSWORD')
while True:
    my_bot.find_posts('THE COMMENT THAT WILL BE POSTED ON EACH RELATED POST')
