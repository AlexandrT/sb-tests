import pytest

from helpers.credit_card.page import *
from helpers.utils import *
from helpers.assertions import *
from faker import Faker


class TestCreditCard(BaseTest):
    """Credit card. """

    def setup_method(self):
        fake = self.fake

        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.middle_name = fake.middle_name()

    def test_fill_form(self, selenium, base_url):
        """Заполнение анкеты."""

        selenium.get(f"{base_url}/credit_card/info")

        credit_card_page = CreditCardPage(selenium)
        credit_card_page.first_name = self.first_name
        credit_card_page.last_name = self.last_name
        credit_card_page.middle_name = self.middle_name
        credit_card_page.click_send_btn()

        assert_field_error(credit_card_page.limit)