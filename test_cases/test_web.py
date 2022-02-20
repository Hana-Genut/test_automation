import pytest
import utilities
from test_cases.conftest import *
from work_flows.table_WF import table_wf
from utilities.read_properties import get_data
from utilities.manage_pages import Page_Manager


@pytest.mark.usefixtures("init_web")
class Test_Web:
    def test_01_verify_text(self):
        self.driver.get(get_data("Url"))
        table = utilities.manage_pages.main_table_PO.table()
        table_wf.verify_table_cell_text(self.driver, table, get_data("search_column"), get_data("search_text"), get_data("return_column_text"), get_data("expected_result"))


