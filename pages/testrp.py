from selenium.webdriver.common.by import By

from pages.base import Base


class TestRp(Base):
    _logout_button_locator = (By.CSS_SELECTOR, '#main-content a[href="/logout"]')

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()
