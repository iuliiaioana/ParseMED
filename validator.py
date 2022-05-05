from lxml import etree


def validate(xml_path: str, xsd_path: str) -> bool:
    """validarea fisierului xml conform schemei xml(xsd)
    :params meds_lst: medicamente
    :type meds_lst: list
    :returns: true/false: valid/invalid
    """
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)
    return result
