def get_table_cell_text_by_xpath(driver, table, search_column, search_text, return_column_text):
    try:
        xpath = "//table[@id='customers']/tbody/tr/td[" + search_column + "][text()='" + search_text + "']/parent::tr/td[" + return_column_text + "]"
        element = driver.find_element_by_xpath(xpath)
        text = element.text
        return text
    except Exception as e:
        print("no such element" + str(e))


class table_wf:
    @staticmethod
    def verify_table_cell_text(driver, table, search_column, search_text, return_column_text, expected_text):
        try:
            actual_text = get_table_cell_text_by_xpath(driver, table, search_column, search_text, return_column_text)
            if actual_text == expected_text:
                return True
        except Exception as e:
            print("test failed" + str(e))
        return False
