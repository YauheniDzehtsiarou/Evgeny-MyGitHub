import pytest

from utils.read_csv import read_csv

valid_username = "tomsmith"
valid_password = "SuperSecretPassword!"

def test_valid_login(login_page):
    home_page = login_page.open() \
                          .valid_login(valid_username,valid_password)
    login_confirmation = home_page.get_notification()
    assert "You logged into" in login_confirmation

    logout_confirmation = home_page.logout().get_notification()
    assert "You logged out" in logout_confirmation

@pytest.mark.parametrize("username, password, error", read_csv('page objects (PO)/invalid.csv'))
def test_invalid_login(login_page, username, password, error):
    login_page.open().invalid_login(username,password)
    error_text = login_page.get_notification()
    assert error in error_text