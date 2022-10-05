# https://stackoverflow.com/questions/67565291/extract-xml-data-from-soap-response-in-python
import os
from zeep import Client
from zeep.exceptions import XMLParseError
from lxml import etree
import requests
from xml.etree import ElementTree


class OSBUtil:
    @staticmethod
    def post(wsdl_url: str, operation_name: str, header_in) -> None:
        try:
            print('Begin execute', operation_name)
            client = Client(wsdl_url)
            headers = {'content-type': 'text/xml'}
            header_in = {'UserName': 'IB', 'Password': 'abcd1234'}
            body = client.create_message(
                client.service, operation_name, _soapheaders={'HeaderIn': header_in})
            print(f"body {body}")
            response = requests.post(wsdl_url, data=etree.tostring(
                body, pretty_print=True), headers=headers)
            if response.status_code == 200:
                return response.content.decode("utf-8")
            elif response.status_code == 500:
                print('Exception from OSB when executed',
                      operation_name, 'status code = 500')
            else:
                print('Exception from OSB when executed', operation_name,
                      'status code =', response.status_code)
        except Exception as ex:
            print('Exception:', ex)
        finally:
            print('Finish execute', operation_name)

    @staticmethod
    def getResponse(operation_name: str, soap_response):
        if soap_response != None:
            root = ElementTree.XML(soap_response)
            # ElementTree.dump(root)
            # print (root.tag)
            for GetWorkingDateResponse in root.findall(
                    f"{{http://schemas.xmlsoap.org/soap/envelope/}}Body/{{http://www.alsb.com/}}{operation_name}Response"):
                # ElementTree.dump(GetWorkingDateResponse)
                PreviousDate = GetWorkingDateResponse.find("PreviousDate").text
                print('PreviousDate', PreviousDate)
                NextDate = GetWorkingDateResponse.find("NextDate").text
                print('NextDate', NextDate)
                WorkingDate = GetWorkingDateResponse.find("WorkingDate").text
                print('WorkingDate', WorkingDate)


operation_name = 'GetWorkingDate'
wsdl_url = 'http://10.128.10.21:8003/EBANK_TUX/RBSServices/CoreBankingService?wsdl'
soap_response = OSBUtil.post2osb(wsdl_url, operation_name)
# print(r1)

# try:

#     print('Begin execute', operation_name)

#     # client = Client(wsdl_url)
#     # headers = {'content-type': 'text/xml'}
#     # HeaderIn = {'UserName': 'IB', 'Password': 'abcd1234'}
#     # body = client.create_message(
#     #     client.service, operation_name, _soapheaders={'HeaderIn': HeaderIn})
#     # print(f"body {body}")
#     # response = requests.post(wsdl_url, data=etree.tostring(
#     #     body, pretty_print=True), headers=headers)
#     # if response.status_code == 200:
#     #     responseString = response.content.decode("utf-8")
#     #     print(f"ResponseString: {responseString}")
#     #     root = ElementTree.XML(responseString)
#     #     # ElementTree.dump(root)
#     #     # print (root.tag)
#     #     for GetWorkingDateResponse in root.findall(
#     #             "{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://www.alsb.com/}GetWorkingDateResponse"):
#     #         ElementTree.dump(GetWorkingDateResponse)
#     #         PreviousDate = GetWorkingDateResponse.find("PreviousDate").text
#     #         print('PreviousDate', PreviousDate)
#     #         NextDate = GetWorkingDateResponse.find("NextDate").text
#     #         print('NextDate', NextDate)
#     #         WorkingDate = GetWorkingDateResponse.find("WorkingDate").text
#     #         print('WorkingDate', WorkingDate)
#     # elif response.status_code == 500:
#     #     print('Exception from OSB when executed',
#     #           operation_name, 'status code = 500')
#     # else:
#     #     print('Exception from OSB when executed', operation_name,
#     #           'status code =', response.status_code)
#     print('Finish execute', operation_name)
# except XMLParseError as ex:
#     print('XMLParseError:', ex.message)
# except Exception as ex:
#     print('Exception:', ex)
