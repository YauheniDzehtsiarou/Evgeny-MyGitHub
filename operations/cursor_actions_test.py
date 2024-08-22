import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def action_builder(driver):
    return ActionChains(driver)

def test_hover_over(driver, action_builder):
    driver.get("https://the-internet.herokuapp.com/hovers")
    user1 = driver.find_element(By.XPATH, "//div[1]/div[1]/h5[1]")
    assert not user1.is_displayed()

    img1 = driver.find_element(By.XPATH, "//div[1]/div[1]/img[1]")
    action_builder.move_to_element(img1).perform()
    assert user1.is_displayed()

def test_move_cursor_with_offset(driver, action_builder):
    driver.get("https://webminal.org/")
    register = driver.find_element(By.LINK_TEXT,"Register")
    action_builder.move_by_offset(register.location["x"]+ 8, register.location["y"]+8) \
        .click().perform() # "\" is used to write long statements in multiple lines
    assert "Join" == driver.find_element(By.XPATH, "//h2[contains(text(),'Join')]").text

def test_drag_and_drop2(driver,action_builder):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    source = driver.find_element(By.ID, "column-a")
    dest = driver.find_element(By.ID, "column-b")
    action_builder.drag_and_drop(source,dest).perform()
    assert "A" == dest.text
    time.sleep(3)

def test_drag_and_drop(driver, action_builder):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    source = driver.find_element(By.ID, "column-b")
    time.sleep(3)
    destination = driver.find_element(By.ID, "column-a")
    time.sleep(3)
    action_builder.drag_and_drop(source, destination).perform()
    assert "B" == destination.text
    time.sleep(5)

def test_right_and_double_click(driver, action_builder):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/dropdown-menu.html")
    right_click_dropdown = driver.find_element(By.ID, "my-dropdown-2")
    action_builder.context_click(right_click_dropdown).perform()
    right_click_dropdown_context_menu = driver.find_element(By.ID, "context-menu-2")
    assert right_click_dropdown_context_menu.is_displayed()
    time.sleep(3)

    double_click_dropdown = driver.find_element(By.ID, "my-dropdown-3")
    action_builder.double_click(double_click_dropdown).perform()
    double_click_dropdown_context_menu = driver.find_element(By.ID, "context-menu-3")
    assert double_click_dropdown_context_menu.is_displayed()