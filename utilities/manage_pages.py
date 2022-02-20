from page_objects.main_table_PO import Table

main_table_PO = None


class Page_Manager:

    def init_web_page(driver):
        globals()['main_table_PO'] = Table(driver)
