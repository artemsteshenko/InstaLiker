from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class StoriesViewer:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def open_stories(self, account_name):
        # self.driver.get(f'https://www.instagram.com/{account_name}/')
        try:
            self.driver.get(f'https://www.instagram.com/stories/{account_name}/')
            self.logger.info(f"Open stories of account '{account_name}' ")
            sleep(2)
        except:
            self.logger.error(f"No stories in the account '{account_name}'")

    def start_viewing(self):
        try:
            button_view_story = self.driver.find_element(By.XPATH, "//*[contains(text(), 'View story')]")
            button_view_story.click()
            self.logger.info(f"Start viewing")
            sleep(2)
            return True
        except:
            self.logger.error(f"Not found button 'View story'")
            return False

    def next_story(self):
        try:
            button_next = self.driver.find_element(By.CSS_SELECTOR, "[aria-label='Next']")
            button_next.click()
            sleep(0.5)
            self.logger.info(f"Vied story")
            return True
        except:
            self.logger.info(f"No more stories in the account")
            return False

    def like(self):
        try:
            button_like = self.driver.find_elements(By.CLASS_NAME, '_abl-')[3]
            # self.logger.info(button_like)
            button_like.click()
            sleep(0.5)
            self.logger.info(f"Liked story")
        except:
            self.logger.error(f"Not found button 'Like'")

    def run(self, account_name, with_liking=True):
        self.open_stories(account_name)
        have_stories = self.start_viewing()
        while have_stories:
            self.like()
            have_stories = self.next_story()

