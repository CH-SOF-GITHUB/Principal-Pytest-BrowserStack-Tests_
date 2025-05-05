import os

def take_screenshot(driver, name):
    os.makedirs(os.path.join("screenshots", os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshots", name))

"""
 browser.save_screenshot(
            'C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\tau-intro-selenium-py\\screenshots\\search-multiple-',
            expected_phrase, '.png')
"""