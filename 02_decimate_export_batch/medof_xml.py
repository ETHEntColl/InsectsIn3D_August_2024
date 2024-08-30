# Modify the cameras.xml file (only necessary for models with medof folder)
import xml.etree.ElementTree as ET

def medof_xml(path):
    # Load the XML file
    tree = ET.parse(path)
    root = tree.getroot()

    # Function to replace text in label attributes
    def replace_label_text(element, old_text, new_text):
        for elem in element.iter():
            if 'label' in elem.attrib:
                elem.attrib['label'] = elem.attrib['label'].replace(old_text, new_text)

    # Replace "inner" and "outer" with "image" in label attributes
    replace_label_text(root, 'inner', 'image')
    replace_label_text(root, 'outer', 'image')

    # Write the modified XML back to the file
    tree.write(path)