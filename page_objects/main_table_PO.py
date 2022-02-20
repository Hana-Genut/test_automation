class Table:
    def __init__(self, driver):
        self.driver = driver

    def table(self):
        return self.driver.find_element_by_xpath("//table[@id='customers']")

    def xpath(self, search_column, search_text, return_column_text):
        return self.driver.find_element_by_xpath("//table[@id='customers']/tbody/tr/td["+search_column+"][text()="+search_text+"]/parent::tr/td["+return_column_text+"]")
