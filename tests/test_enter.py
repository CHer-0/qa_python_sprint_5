from links import Links
import pytest
from locators import TestLocators


class TestEnter:

    @pytest.mark.parametrize('url, button', [['', TestLocators.ENTER_AUTH],
                                             ['', TestLocators.PERSONAL_CAB],
                                             ['register', TestLocators.BLUE_ENTER],
                                             ['forgot-password', TestLocators.BLUE_ENTER]
                                             ]
                             )
    def test_enter_by_any_button(self, driver, url, button):
        driver.get(Links.MAIN + url)
        driver.find_element(*button).click()
        assert driver.current_url == Links.LOGIN

