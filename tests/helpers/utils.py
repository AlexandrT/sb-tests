import pytest

from faker import Faker


@pytest.mark.nondestructive
class BaseTest(object):
    def setup_class(cls):
        cls.fake = Faker('ru_RU')