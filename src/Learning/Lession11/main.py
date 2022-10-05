from dataclasses import dataclass
from typing import List

from lxml import etree  # type: ignore
from xml_dataclasses import xml_dataclass, rename, load, dump, NsMap, XmlDataclass

CONTAINER_NS = "urn:oasis:names:tc:opendocument:xmlns:container"


@xml_dataclass
@dataclass
class RootFile:
    __ns__ = CONTAINER_NS
    full_path: str = rename(name="full-path")
    media_type: str = rename(name="media-type")


@xml_dataclass
@dataclass
class RootFiles:
    __ns__ = CONTAINER_NS
    rootfile: List[RootFile]


# see Gotchas, this workaround is required for type hinting
@xml_dataclass
@dataclass
class Container(XmlDataclass):
    __ns__ = CONTAINER_NS
    version: str
    rootfiles: RootFiles

    # WARNING: this is an incomplete implementation of an OPF container

    def xml_validate(self) -> None:
        pass
        # if self.version != "1.0":
        #     raise ValueError(f"Unknown container version '{self.version}'")


if __name__ == "__main__":
    nsmap: NsMap = {None: CONTAINER_NS}
    # see Gotchas, stripping whitespace and comments is highly recommended
    parser = etree.XMLParser(remove_blank_text=True, remove_comments=True)
    lxml_el_in = etree.parse("container.xml", parser).getroot()
    container: Container = load(Container, lxml_el_in, "container")
    print (container.version)
    lxml_el_out = dump(container, "container", nsmap)
    print(etree.tostring(lxml_el_out, encoding="unicode", pretty_print=True))
