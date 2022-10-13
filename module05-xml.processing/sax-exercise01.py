import xml.sax

from world.domain import Country


class CountryHandler(xml.sax.ContentHandler):
    def __init__(self, predicate, sorter):
        self._countries = []
        self._predicate = predicate
        self._sorter = sorter
        self._country = Country()
        self._open_tag = ""
        self._property_tag_mapper = {
            "Code": "code",
            "Name": "name",
            "Continent": "continent",
            "SurfaceArea": "surfaceArea",
            "Population": "population"
        }

    @property
    def countries(self):
        return self._countries

    @property
    def predicate(self):
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        self._predicate = predicate

    @property
    def sorter(self):
        return self._sorter

    @sorter.setter
    def sorter(self, sorter):
        self._sorter = sorter

    def startElement(self, tag, attributes):
        self._open_tag = tag

    def startDocument(self):
        self._countries = []

    def endDocument(self):
        self._countries.sort(key=self.sorter)

    def endElement(self, tag):
        self._open_tag = ""
        if tag == "country":
            if self._predicate(self._country):
                self._countries.append(self._country)
                self._country = Country()

    def characters(self, content):
        if self._open_tag in self._property_tag_mapper.keys():
            property_name = self._property_tag_mapper[self._open_tag]
            setattr(self._country, property_name, content)


parser = xml.sax.make_parser()
handler = CountryHandler(lambda ctry: ctry.continent == "Europe", lambda ctry: ctry.name)
parser.setContentHandler(handler)
parser.parse("resources/countries.xml")
for country in handler.countries:
    print(country)
print("\nFinding populated countries....\n")
handler.predicate = lambda ctry: ctry.population > 100000000
handler.sorter = lambda ctry: ctry.population
parser.parse("resources/countries.xml")
for country in handler.countries:
    print(country)
