from selenium.webdriver.support import ui


def close_cookies_popup(driver):
    close_cookies_popup_button = ui.WebDriverWait(driver, 30).until(
        lambda d: d.find_element_by_css_selector('#stravaCookieBanner .btn-dismiss-cookie-banner'))
    close_cookies_popup_button.click()


def login(driver):
    driver.get('https://www.strava.com/')
    login_button = driver.find_element_by_css_selector('.btn.btn-default.btn-login')
    close_cookies_popup(driver)
    login_button.click()
    print('Please log into your Strava account')
    ui.WebDriverWait(driver, 86400).until(lambda d: d.find_element_by_id('notifications'))
