from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def sort_trainings_descending(driver):
    sorting_switch = ui.WebDriverWait(driver, 30).until(
        lambda d: d.find_element_by_css_selector('.active.text-capitalize'))
    sorting_switch_class = sorting_switch.get_attribute('class')
    if 'desc' in sorting_switch_class:
        sorting_switch.click()


def enter_first_training(driver):
    sort_trainings_descending(driver)
    training_link = ui.WebDriverWait(driver, 30).until(
        lambda d: d.find_element_by_css_selector('.row.history-list__row > div.exercise-link'))
    training_link.click()


class NoMoreTrainingsException(Exception):
    pass


def go_to_previous_training(driver):
    previous_button_group = ui.WebDriverWait(driver, 30).until(
        lambda d: d.find_element_by_css_selector('.usr-navigation-details .nav.nav-pills.inline-block > li'))
    if 'disabled' in previous_button_group.get_attribute('class'):
        raise NoMoreTrainingsException()
    previous_button = previous_button_group.find_element_by_css_selector('a')
    ui.WebDriverWait(driver, 30).until(lambda _: previous_button.is_enabled() and previous_button.is_displayed())
    ui.WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div#loading-spinner')))
    previous_button.click()


def download_current_training(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    export_session_button = ui.WebDriverWait(driver, 30).until(
        lambda d: d.find_element_by_css_selector('a#exportTrainingSessionPopup'))
    ui.WebDriverWait(driver, 30).until(
        lambda _: export_session_button.is_enabled() and export_session_button.is_displayed())
    ui.WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div#loading-spinner')))
    export_session_button.click()

    export_popup = driver.find_element_by_css_selector('div#flow_overlay')
    ui.WebDriverWait(driver, 30).until(lambda _: not export_popup.get_attribute('style').startswith("z-index: -1;"))
    tcx_session_button = export_popup\
        .find_element_by_css_selector('.exportTrainingSession__item__description.info-line-wrapper.force-wrap > a')
    tcx_session_button.click()

    export_popup_close_button = export_popup.find_element_by_css_selector('.pull-right.modal-close')
    export_popup_close_button.click()


def download_trainings(driver):
    diary_list_button = driver.find_element_by_id('diary_list')
    diary_list_button.click()
    ui.WebDriverWait(driver, 30).until(lambda d: driver.find_element_by_id('historyStart'))
    enter_first_training(driver)
    driver.switch_to.window(driver.window_handles[1])
    try:
        i = 0
        while True:
            download_current_training(driver)
            go_to_previous_training(driver)
            i += 1
            if i == 5:
                break
    except NoMoreTrainingsException:
        pass
