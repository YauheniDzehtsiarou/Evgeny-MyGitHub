import time
import pytest

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get('https://www.selenium.dev/selenium/docs/api/py/api.html')


def test_scrolling(driver):
#JS script
# x = 0, y= document.body.scrollHeight - height of scrollable pixels
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #return height from JS to PY
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
#from PY to JS
    new_height = 1000
    driver.execute_script("window.scrollTo(0, arguments[0])",new_height)
    time.sleep(3)