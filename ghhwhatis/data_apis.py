############################################## BEAUTIFULSOUP
import urllib2
from bs4 import BeautifulSoup
from suds.client import Client

#SUBJECT 1
def get_subject_one_data(data):
    subject_one_dict = {}
    subject_one_wiki_url = "http://en.wikipedia.org/w/api.php?action=opensearch&limit=1&namespace=0&format=xml&search={0}"\
        .format(data)
    req1 = urllib2.Request(subject_one_wiki_url)
    resp1 = urllib2.urlopen(req1)
    xml1 = resp1.read()
    soup1 = BeautifulSoup(xml1)
    subject_one_dict['query'] = soup1.query.text
    subject_one_dict['description'] = soup1.description.text
    return subject_one_dict


#SUBJECT 2
def get_subject_two_data(data):
    subject_two_dict = {}
    subject_two_wiki_url = "http://en.wikipedia.org/w/api.php?action=opensearch&limit=1&namespace=0&format=xml&search={0}"\
        .format(data)
    req2 = urllib2.Request(subject_two_wiki_url)
    resp2 = urllib2.urlopen(req2)
    xml2 = resp2.read()
    soup2 = BeautifulSoup(xml2)
    subject_two_dict['query'] = soup2.query.text
    subject_two_dict['description'] = soup2.description.text
    return subject_two_dict

def get_subject_one_data_dictservice(data):
    subject_one_dict_dictservice = {}
    client = Client('http://services.aonaware.com/DictService/DictService.asmx?WSDL')
#    print client.service.Define(data)
    subject_one_dict_dictservice['query'] = client.service.Define(data)[0]
    subject_one_dict_dictservice['datalist'] = [[d.Dictionary.Name,d.WordDefinition]
                                                for d in client.service.Define(data)[1].Definition]
    subject_one_data = {}
    subject_one_source_list = []
    subject_one_data_list = []

    for datasource, datavalue in subject_one_dict_dictservice['datalist']:
         subject_one_source_list.append(datasource)
         subject_one_data_list.append(datavalue)
        
    subject_one_data['sources'] = subject_one_source_list
    subject_one_data['data'] = subject_one_data_list

    print '<br />'.join(subject_one_data['sources'])
    print ''.join(subject_one_data['data'])

get_subject_one_data_dictservice('new york')