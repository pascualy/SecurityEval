from lxml import etree
import requests

def transform_xml(url, username, password):
    '''
    create an XML parser, parse from a URL
    transform it providing access control from network
    :param url: str, the URL to the XML file
    :param username: str, the username for access control
    :param password: str, the password for access control
    :return: str, the transformed XML
    '''
    # create a requests session
    session = requests.Session()

    # set the username and password for the session
    session.auth = (username, password)

    # get the XML from the URL
    response = session.get(url)

    # create an XML parser and parse the XML
    parser = etree.XMLParser()
    root = etree.fromstring(response.content, parser=parser)

    # TODO: implement transformation logic

    # return the transformed XML
    return etree.tostring(root, pretty_print=True)