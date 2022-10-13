import xml.sax


class CountryHandler(xml.sax.ContentHandler):
    def __init__(self):

    def startElement(self, tag, attributes):
        print(f"New opening tag: {tag}")

    def endElement(self, tag):
        print(f"Closing opening tag: {tag}")


parser = xml.sax.make_parser()
handler = CountryHandler()
parser.setContentHandler(handler)
parser.parse("resources/countries.xml")
