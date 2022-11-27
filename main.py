import pickle
import argparse
from time import sleep, time
from random import uniform

from selenium.webdriver.common.by import By
from loguru import logger

from auth import auth_with_cookies, auth_with_credentials
from stories_viewer import StoriesViewer
from proxy import get_chromedriver

parser = argparse.ArgumentParser()

parser.add_argument("login", help="login")
parser.add_argument("password", help="password")

parser.add_argument("proxy_host", help="proxy_host")
parser.add_argument("proxy_port", help="proxy_port")
parser.add_argument("proxy_user", help="proxy_user")
parser.add_argument("proxy_password", help="proxy_password")

args = parser.parse_args()
login = args.login
password = args.password

proxy_host = args.proxy_host
proxy_port = args.proxy_port
proxy_user = args.proxy_user
proxy_password = args.proxy_password


driver = get_chromedriver(proxy_host, proxy_port, proxy_user, proxy_password, debug=True)
# driver = webdriver.Safari()

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(10)
try:
    button_accept_cookies = driver.find_element(By.XPATH, "//*[contains(text(), 'Allow essential and optional cookies')]")
    button_accept_cookies.click()
    sleep(4)
except:
    pass

try:
    auth_with_cookies(driver, login, cookie_path='cookies')
except:
    auth_with_credentials(driver, login, password, cookie_path='cookies')


logger.add(f"logs/file_{time()}.log")

with open('data/target_users_with100media.pickle', 'rb') as file:
    users = pickle.load(file)
sleep(10)
viewer = StoriesViewer(driver, logger, (4, 5))
for account_name in users[:10000]:
    viewer.run(account_name=account_name)
    sleep(uniform(0.1, 0.3))