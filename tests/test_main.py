from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_first_page(browser):
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Desktops')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Laptops & Notebooks')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Components')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tablets')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Software')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Phones & PDAs')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Cameras')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'MP3 Players')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'MacBook')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'iPhone')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Apple Cinema 30"')), message='')
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Apple Cinema 30"')), message='')
    assert "Your Store" == browser.title


def test_search(browser):
    search = browser.find_element(By.XPATH, '//*[@id="search"]/span')
    search.click()
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")), message='')
    assert "Search" == browser.title
