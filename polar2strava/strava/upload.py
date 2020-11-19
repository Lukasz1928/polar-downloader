from polar2strava.common.driver import get_driver
from polar2strava.strava import login


def upload():
    driver = get_driver()
    login(driver)