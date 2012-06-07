############################################## BEAUTIFULSOUP
import urllib2
from bs4 import BeautifulSoup

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

#print get_subject_one_data('spinach')['query']
#print get_subject_two_data('kale')['query']
#
#print get_subject_one_data('spinach')['description']
#print get_subject_two_data('kale')['description']

#obj, created = DifferncePage.objects.get_or_create(subject_one='John', subject_two='Lennon',
#                  defaults={'birthday': date(1940, 10, 9)})