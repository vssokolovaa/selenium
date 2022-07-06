from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_register(browser, url):
    browser.get(f"{url}index.php?route=account/register")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content>h1')), message='Register Account')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#account>legend')), message='Your Personal Details')
    wait.until(EC.visibility_of_element_located((By.ID, 'input-firstname')), message='First Name')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'fieldset:nth-child(2)>legend')),
               message='Your Password')
    wait.until(EC.visibility_of_element_located((By.ID, 'input-password')), message='Password')
