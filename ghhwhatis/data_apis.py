############################################## BEAUTIFULSOUP
import urllib2
from bs4 import BeautifulSoup
from suds.client import Client
import requests

#SUBJECT 1
def get_subject_one_data(data):
    subject_one_dict = {}
    try:
        subject_one_wiki_url = "http://en.wikipedia.org/w/api.php?action=opensearch&limit=1&namespace=0&format=xml&search={0}"\
            .format(data)
        req1 = urllib2.Request(subject_one_wiki_url)
        resp1 = urllib2.urlopen(req1)
        xml1 = resp1.read()
        soup1 = BeautifulSoup(xml1)
        subject_one_dict['query'] = soup1.query.text
        subject_one_dict['description'] = soup1.description.text
    except AttributeError:
        subject_one_dict['query'] = data
        subject_one_dict['description'] = ""

    return subject_one_dict


#SUBJECT 2
def get_subject_two_data(data):
    subject_two_dict = {}
    try:
        subject_two_wiki_url = "http://en.wikipedia.org/w/api.php?action=opensearch&limit=1&namespace=0&format=xml&search={0}"\
            .format(data)
        req2 = urllib2.Request(subject_two_wiki_url)
        resp2 = urllib2.urlopen(req2)
        xml2 = resp2.read()
        soup2 = BeautifulSoup(xml2)
        subject_two_dict['query'] = soup2.query.text
        subject_two_dict['description'] = soup2.description.text
    except AttributeError:
        subject_two_dict['query'] = data
        subject_two_dict['description'] = ""
    return subject_two_dict

def get_subject_one_data_dictservice(data):
    subject_one_data = {}
    subject_one_source_list = []
    subject_one_data_list = []
    try:
        subject_one_dict_dictservice = {}
        client = Client('http://services.aonaware.com/DictService/DictService.asmx?WSDL')
    #    print client.service.Define(data)
        subject_one_dict_dictservice['query'] = client.service.Define(data)[0]
        subject_one_dict_dictservice['datalist'] = [[d.Dictionary.Name,d.WordDefinition]
                                                    for d in reversed(client.service.Define(data)[1].Definition)]

        for datasource, datavalue in subject_one_dict_dictservice['datalist']:
             subject_one_source_list.append("<li><em>{0}</em>: {1}</li>".format(data, datasource))
             subject_one_data_list.append("<p>{0}</p>".format(datavalue))

        subject_one_data['sources'] = subject_one_source_list
        subject_one_data['data'] = subject_one_data_list
    except AttributeError:
        subject_one_data['sources'] = ""
        subject_one_data['data'] = "Additional data for {0} on the way. Please check back soon.".format(data)
    return subject_one_data


def get_subject_two_data_dictservice(data):
    subject_two_data = {}
    subject_two_source_list = []
    subject_two_data_list = []
    try:
        subject_two_dict_dictservice = {}
        client = Client('http://services.aonaware.com/DictService/DictService.asmx?WSDL')
    #    print client.service.Define(data)
        subject_two_dict_dictservice['query'] = client.service.Define(data)[0]
        subject_two_dict_dictservice['datalist'] = [[d.Dictionary.Name,d.WordDefinition]
                                                    for d in reversed(client.service.Define(data)[1].Definition)]

        for datasource, datavalue in subject_two_dict_dictservice['datalist']:
             subject_two_source_list.append("<li><em>{0}</em>: {1}</li>".format(data,datasource))
             subject_two_data_list.append("<p>{0}</p>".format(datavalue))

        subject_two_data['sources'] = subject_two_source_list
        subject_two_data['data'] = subject_two_data_list
    except AttributeError:
        subject_two_data['sources'] = ""
        subject_two_data['data'] = "Additional data for {0} on the way. Please check back soon.".format(data)
    return subject_two_data

#print get_subject_one_data('new york')
#print get_subject_two_data('los angeles')

#print get_subject_one_data_dictservice('new york')['data']
#print get_subject_two_data_dictservice('#lksdf')['data']

#print ''.join(get_subject_one_data_dictservice('wers')['data'])
#print ''.join(get_subject_two_data_dictservice('los angeles')['data'])