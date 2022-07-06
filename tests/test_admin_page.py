from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    USERNAME = (By.ID, 'input-username')
    PASSWORD = (By.ID, 'input-password')
    BUTTON = (By.TAG_NAME, 'button')


def test_admin_find(browser, url):
    browser.get(f"{url}admin")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-title')),
               message=' Please enter your login details.')
    wait.until(EC.visibility_of_element_located(Page.USERNAME), message='')
    wait.until(EC.visibility_of_element_located(Page.PASSWORD), message='')
    wait.until(EC.visibility_of_element_located(Page.BUTTON), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgotten Password')), message='')
