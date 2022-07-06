from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_card(browser):
    macbook = browser.find_element(By.LINK_TEXT, "MacBook")
    macbook.click()
    wait = WebDriverWait(browser, 15, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "MacBook")), message='')
    add_cart = browser.find_element(By.ID, "button-cart")
    add_cart.click()
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                           'div.alert.alert-success.alert-dismissible')),
                         message='')

    assert "MacBook" == browser.title
    assert element.text == 'Success: You have added MacBook to your shopping cart!\n×'
