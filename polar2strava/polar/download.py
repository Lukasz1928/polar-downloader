from polar2strava.common.driver import get_driver
from polar2strava.polar import login
from polar2strava.polar.trainings import download_trainings


def download():
    driver = get_driver()
    login(driver)
    download_trainings(driver)

