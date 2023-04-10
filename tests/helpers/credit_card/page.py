from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class LastName(BaseElement):
    locator = CreditCardPageLocators.LAST_NAME_INPUT


class FirstName(BaseElement):
    locator = CreditCardPageLocators.FIRST_NAME_INPUT


class MiddleName(BaseElement):
    locator = CreditCardPageLocators.MIDDLE_NAME_INPUT


class Limit(BaseElement):
    locator = CreditCardPageLocators.LIMIT_INPUT

class CreditCardPage(BasePage):
    last_name = LastName()
    first_name = FirstName()
    middle_name = MiddleName()
    limit = Limit()

    def click_send_btn(self):
        element = self.driver.find_element(*CreditCardPageLocators.SEND_BUTTON)
        element.click()