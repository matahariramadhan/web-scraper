from xml.etree import ElementTree as ET


def list_to_hierarchical_dict(datas: list):
    '''Convert list to hierarchical dictionary'''

    def recursive(data):
        d = {}
        if len(data) == 2:
            key = data[0]
            value = data[1]
            d[key] = value

        else:
            key = data[0]
            value = recursive(data[1:])

            d[key] = value

        return d

    return recursive(datas)


def dict_to_xml(data: dict, parent) -> ET.Element:
    for key in data:
        if type(data[key]) is dict:
            tag = ET.SubElement(parent, str(key).replace(' ', '_'))
            dict_to_xml(data[key], tag)
        else:
            tag = ET.SubElement(parent, str(key).replace(
                ' ', '_')).text = str(data[key])
    return parent
