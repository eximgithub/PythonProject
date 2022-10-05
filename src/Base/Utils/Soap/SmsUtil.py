from datetime import datetime
import uuid
import xmltodict
from lxml import etree  # type: ignore
from dataclasses import dataclass, field
from typing import Optional

from Base.Utils.XML.XMLUtil import XMLUtil
from Base.Utils.Soap.SoapUtil import SoapUtil


@dataclass(init=False)
class SMSRequest:
    ClientId: Optional[str] = field(metadata=dict(type="Element", required=True))
    ReferenceNo: Optional[str] = field(metadata=dict(type="Element", required=True))
    PhoneNumber: Optional[str] = field(metadata=dict(type="Element", required=True))
    OTTPhoneNumber: Optional[str] = field(metadata=dict(type="Element"))
    Message: Optional[str] = field(metadata=dict(type="Element"))
    RequestTime: Optional[str] = field(metadata=dict(type="Element"))
    CustId: Optional[str] = field(metadata=dict(type="Element"))
    SendType: Optional[str] = field(metadata=dict(type="Element", required=True))


@dataclass
class SMSResponse:
    ReferenceNo: Optional[str] = field(metadata=dict(type="Element"))
    ErrorCode: Optional[str] = field(metadata=dict(type="Element"))
    ErrorDesc: Optional[str] = field(metadata=dict(type="Element"))
    ResponseTime: Optional[str] = field(metadata=dict(type="Element"))


class SmsUtil:
    @staticmethod
    def send_sms(wsdl_url: str, sms_request: SMSRequest) -> SMSResponse:
        operation_name = 'SendSMS'
        sms_request_as_string = XMLUtil.Serialize(sms_request)
        response = SoapUtil.post(wsdl_url, operation_name, sms_request_as_string)
        if response.status_code == 200:
            stack_d = xmltodict.parse(response.content)
            sms_response_as_string = stack_d['soap:Envelope']['soap:Body']['SendSMSResponse']['SendSMSResult']
            sms_response: SMSResponse = XMLUtil.Deserialize(sms_response_as_string, SMSResponse)
            return sms_response
        elif response.status_code == 500:
            print('Exception from web service when executed',
                  operation_name, 'status code = 500')
            return None
        else:
            print('Exception from web service when executed', operation_name,
                  'status code =', response.status_code)
            return None


wsdl_url = 'http://10.128.133.17/FISMSGatewayOthers/Service.asmx?WSDL'
sMSRequest = SMSRequest()
sMSRequest.ClientId = "EOfficeService"
sMSRequest.ReferenceNo = str(uuid.uuid4())
sMSRequest.PhoneNumber = "84903083166"
sMSRequest.OTTPhoneNumber = "84903083166"
sMSRequest.Message = "hoang.ln test python"
sMSRequest.RequestTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sMSRequest.CustId = "118816270"
sMSRequest.SendType = "2"
sMSResponse = SmsUtil.send_sms(wsdl_url, sMSRequest)
# pprint.pprint(sMSResponse)

sMSRequestAsString = XMLUtil.Serialize(sMSRequest)
print(sMSRequestAsString)
sMSResponseAsString = XMLUtil.Serialize(sMSResponse)
print(sMSResponseAsString)
