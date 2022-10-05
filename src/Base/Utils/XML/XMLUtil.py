from typing import Optional, TypeVar, Type

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

T = TypeVar("T")


class XMLUtil:
    __xml_deserializer = XmlParser(config=ParserConfig(fail_on_unknown_properties=True))
    __xml_serializer = XmlSerializer()

    @staticmethod
    def Serialize(source):
        return XMLUtil.__xml_serializer.render(source)

    @staticmethod
    def Deserialize(source: str, clazz: Optional[Type[T]] = None):
        return XMLUtil.__xml_deserializer.from_string(source, clazz)
