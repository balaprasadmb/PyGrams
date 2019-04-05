import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
print root.getchildren()
for i in root.getiterator():
    print i
print root.items()
print root.keys()
print root.tag
print root.tail()
print root.text()
