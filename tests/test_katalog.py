from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog(browser):
    desktop = browser.find_element(By.LINK_TEXT, 'Desktops')
    desktop.click()
    all_desktop = browser.find_element(By.LINK_TEXT, 'Show All Desktops')
    all_desktop.click()
    wait = WebDriverWait(browser, 15, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")), message='Caption')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-left>div.list-group>a:nth-child(2)")),
               message='- PC (0)')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-left>div.list-group>a:nth-child(3)")),
               message='- Mac (1)')
