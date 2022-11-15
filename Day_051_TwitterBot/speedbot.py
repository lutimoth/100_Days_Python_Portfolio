from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = os.getenv("PROMISED_DOWN")
PROMISED_UP = os.getenv("PROMISED_UP")
CHROME_DRIVER_PATH = os.getenv("CHROME_PATH")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PW")

class InternetSpeedTwitterBot:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH))
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()