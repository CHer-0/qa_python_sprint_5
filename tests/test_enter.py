import pytest
from locators import TestLocators


class TestEnter:
    main_url = 'https://stellarburgers.nomoreparties.site/'

    @pytest.mark.parametrize('url, button', [['', TestLocators.ENTER_AUTH],
                                             ['', TestLocators.PERSONAL_CAB],
                                             ['register', TestLocators.BLUE_ENTER],
                                             ['forgot-password', TestLocators.BLUE_ENTER]
                                             ]
                             )
    def test_enter_by_any_button(self, driver, url, button):
        driver.get(self.main_url + url)
        driver.find_element(*button).click()
        assert driver.current_url == self.main_url + 'login'

