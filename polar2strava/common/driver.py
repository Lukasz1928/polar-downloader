from selenium import webdriver

from polar2strava.common.files import download_location


def get_driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--private")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", download_location)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    driver = webdriver.Firefox(firefox_profile=profile)
    return driver
