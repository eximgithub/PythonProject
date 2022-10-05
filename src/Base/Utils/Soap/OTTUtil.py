from datetime import datetime
import uuid
import xmltodict
from lxml import etree  # type: ignore
from dataclasses import dataclass, field
from typing import Optional

from Base.Utils.XML.XMLUtil import XMLUtil
from Base.Utils.Soap.SoapUtil import SoapUtil
from dataclass_wizard import JSONWizard
import logging
import logging.config


@dataclass(init=False)
class OTTRequest(JSONWizard):
    type: Optional[str] = field(metadata=dict(type="Element"))
    content: Optional[str] = field(metadata=dict(type="Element", required=True))
    mobile: Optional[str] = field(metadata=dict(type="Element", required=True))
    cif: Optional[str] = field(metadata=dict(type="Element", required=True))
    messageId: Optional[str] = field(metadata=dict(type="Element", required=True))
    priority: Optional[str] = field(metadata=dict(type="Element"))
    mediaUrl: Optional[str] = field(metadata=dict(type="Element"))
    mediaType: Optional[str] = field(metadata=dict(type="Element"))
    expireTime: Optional[str] = field(metadata=dict(type="Element", required=True))
    messageTime: Optional[str] = field(metadata=dict(type="Element", required=True))
    isEncrypt: Optional[str] = field(metadata=dict(type="Element"))


@dataclass()
class OTTResponse(JSONWizard):
    referenceNo: Optional[str] = field(metadata=dict(type="Element"))
    requestTime: Optional[str] = field(metadata=dict(type="Element"))
    errorCode: Optional[str] = field(metadata=dict(type="Element"))
    errorDesc: Optional[str] = field(metadata=dict(type="Element"))
    responseTime: Optional[str] = field(metadata=dict(type="Element"))


class OTTUtil:
    @staticmethod
    def send(url: str, req: OTTRequest) -> OTTResponse:
        operation_name = 'sendOTT'
        request_as_string = req.to_json()
        soap_response = SoapUtil.post(url, operation_name, request_as_string)
        if soap_response.status_code == 200:
            stack_d = xmltodict.parse(soap_response.content)
            response_as_string = stack_d['soap:Envelope']['soap:Body']['sendOTTResponse']['sendOTTResult']
            res: OTTResponse = OTTResponse.from_json(response_as_string)
            return res
        elif soap_response.status_code == 500:
            print('Exception from web service when executed',
                  operation_name, 'status code = 500')
            return None
        else:
            print('Exception from web service when executed', operation_name,
                  'status code =', soap_response.status_code)
            return None


def main():
    # load logging.conf
    logging.config.fileConfig('logging.conf')
    # # create logger
    logger = logging.getLogger(__name__)

    wsdl_url = 'http://10.128.133.17/OTTGateway/Service.asmx?WSDL'
    for x in range(1, 1000):
        request = OTTRequest()
        request.type = "16"
        request.content = f"hoang.ln test python {str(x)}"
        request.mobile = "84903083166"
        request.cif = "118816270"
        request.messageId = str(uuid.uuid4())
        request.priority = "2"
        request.mediaUrl = ""
        request.mediaType = ""
        request.expireTime = ""
        request.messageTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.isEncrypt = "0"
        response = OTTUtil.send(wsdl_url, request)
        # pprint.pprint(sMSResponse)

        requestAsString = XMLUtil.Serialize(request)
        logger.info(requestAsString)
        responseAsString = XMLUtil.Serialize(response)
        logger.info(responseAsString)


if __name__ == '__main__':
    main()
