import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse(r'C:\Automation\python_automation\configurations\config.xml').getroot()
    return root.find(".//" + node_name).text
