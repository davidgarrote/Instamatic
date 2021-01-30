# Instamatic
Instagram automation that reproduces real human behaviour. ONLY for research purposes.

How it works?

Instamatic is a simple but effective python script that controls your browser with selenium. Once you have added your credentials to the correct fields, it will:

1. Load Instagram and accept cookies in case there are some. 
2. Log in with the username and password provided
3. Decline notifications in case there are some.
4. Load the latest posts for your search keyword
5. Open the latest post
6. Like the post, leave a comment and follow the user
7. You will be prompted with the total amount of likes, comments and follows of your session
8. The bot will wait for 2 minutes before repeating the process over again, to avoid being banned instantly.

Requirements

Python 3.8+ - https://www.python.org/downloads/
Selenium - https://www.selenium.dev/downloads/
ChromeDriver or the selenium driver for your preferred browser - https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
Read the code and customize it with you credentials and search keywords (everything in capital letters)

Notes:
Due to the high amount of new accounts you'd be following after using this script I recommend using my other script that automates the unfollowing process, replicating the human behaviour.

