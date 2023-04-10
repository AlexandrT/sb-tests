from selenium.webdriver.common.by import By


class CreditCardPageLocators():
    LIMIT_INPUT = (By.XPATH, '//div[@id="contact-info"]/*//label[contains(text(), "лимит")]/following-sibling::div/input')
    FIRST_NAME_INPUT = (By.XPATH, '//div[@id="contact-info"]/*//label[contains(text(), "фамилия")]/following-sibling::div/input')
    LAST_NAME_INPUT = (By.XPATH, '//div[@id="contact-info"]/*//label[contains(text(), "имя")]/following-sibling::div/input')
    MIDDLE_NAME_INPUT = (By.XPATH, '//div[@id="contact-info"]/*//label[contains(text(), "отчество")]/following-sibling::div/input')

    SEND_BUTTON = (By.XPATH, '//div[@id="btnGroupCredit"]/button')