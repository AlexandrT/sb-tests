def assert_field_error(element):
    el_class = element.get_attribute('class')
    if 'input_error' not in el_class:
        raise AssertionError("Input should contains error")
