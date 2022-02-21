import xml.etree.ElementTree as ET

import os
from python_automation.configurations.definitions import ROOT_DIR


def get_data(node_name):
    root = ET.parse(os.path.join(ROOT_DIR, 'configurations', 'config.xml')).getroot()
    return root.find(".//" + node_name).text
