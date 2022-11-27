import pickle
import time
import tempfile
import os
import selenium.common.exceptions as excp
from time import sleep
from random import uniform
from selenium.webdriver.common.by import By


def auth_with_cookies(browser, login, cookie_path=tempfile.gettempdir()):
    # logger.save_screen_shot(browser, 'login.png')

    # logger.log('Trying to auth with cookies.')
    cookies = pickle.load(open(os.path.join(cookie_path, login + '.pkl'), "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
    if check_if_user_authenticated(browser):
        # logger.log("Successful authorization with cookies.")
        return True
    # logger.log("Unsuccessful authorization with cookies.")
    return False


def auth_with_credentials(browser, login, password, cookie_path=tempfile.gettempdir()):
    # logger.log('Trying to auth with credentials.')
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(uniform(0.3, 1))

    login_field = browser.find_element(By.NAME, 'username')
    login_field.clear()
    sleep(uniform(0.6, 1))
    login_field.send_keys(login)
    sleep(uniform(0.6, 1))
    # logger.log("--->AuthWithCreds: filling username.")

    password_field = browser.find_element(By.NAME, "password")
    password_field.clear()
    sleep(uniform(0.6, 1))
    password_field.send_keys(password[0])
    sleep(uniform(0.6, 1))
    password_field.send_keys(password[1:])
    sleep(uniform(0.6, 1))
    # logger.log("--->AuthWithCreds: filling password.")

    submit = browser.find_element(By.CSS_SELECTOR, "form button")
    submit.submit()
    # logger.log("--->AuthWithCreds: submitting login form.")
    sleep(uniform(0.6, 1))
    # logger.log("--->AuthWithCreds: saving cookies.")
    pickle.dump([browser.get_cookies()], open(os.path.join(cookie_path, login + '.pkl'), "wb"))
    # print(browser.get_cookies()[-1])
    if check_if_user_authenticated(browser):
        # logger.log("Successful authorization with credentials.")
        return True
    # logger.log("Unsuccessful authorization with credentials.")
    return False


def check_if_user_authenticated(browser):
    try:
        browser.find_element(By.CSS_SELECTOR, ".coreSpriteDesktopNavProfile")
        return True
    except excp.NoSuchElementException:
        return False