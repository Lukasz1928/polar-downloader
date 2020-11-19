import time
import selenium.webdriver.support.ui as ui


def close_cookies_popup(driver):
    accept_cookies_button = ui.WebDriverWait(driver, 30).until(lambda d: d.find_element_by_css_selector('button#onetrust-accept-btn-handler'))
    time.sleep(5)  # the window reappears if clicked too quickly
    driver.execute_script("arguments[0].click();", accept_cookies_button)


def login(driver):
    driver.get('https://flow.polar.com/')
    login_button = driver.find_element_by_id('loginButtonNav')
    login_button.click()
    close_cookies_popup(driver)
    print('Please log into your Flow account')
    ui.WebDriverWait(driver, 86400).until(lambda d: d.find_element_by_id('diary_list'))
