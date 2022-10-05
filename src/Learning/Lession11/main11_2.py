# https://xsdata.readthedocs.io/en/v20.7/dataclasses.html#parserconfig

import pprint
# from docs.examples.primer import PurchaseOrder, Items, Usaddress
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

@dataclass
class ColorType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

@dataclass
class Test:
    Value: Optional[int] = field(
        # default=None,
        metadata=dict(
            type="Element",
            # namespace="",
            # required=True
        )
    )

@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


# serializer = XmlSerializer(pretty_print=True)
config = ParserConfig(fail_on_unknown_properties=True)
parser = XmlParser(config=config)
order = parser.from_string("<Test><Value>2</Value></Test>", Test)
print(order.Value)