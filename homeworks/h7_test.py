import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/drag-and-drop.html")

@pytest.fixture(autouse=True)
def action_builder(driver):
    return ActionChains(driver)

def test_drag_and_drop(driver, action_builder):
    panel = driver.find_element(By.ID, 'draggable')
    x_before_move = panel.location['x']
    y_before_move = panel.location['y']

    offset_x = 67
    offset_y = 67

    action_builder.click_and_hold(panel) \
        .move_by_offset(offset_x, offset_y) \
        .release() \
        .perform()
    # option2
    # action_builder.drag_and_drop_by_offset(panel,offset_x,offset_y)

    x_after_move = panel.location['x']
    y_after_move = panel.location['y']
    assert x_after_move-x_before_move == offset_x
    assert y_after_move-y_before_move == offset_y