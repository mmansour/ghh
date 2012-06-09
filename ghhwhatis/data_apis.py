############################################## BEAUTIFULSOUP
import urllib2
from bs4 import BeautifulSoup
import json

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

def get_subject_one_data_wordnik(data):
    subject_one_dict_worknik = {}
    subject_one_wiki_url_worknik = "http://api.wordnik.com/v4/word.json/{0}/definitions?includeRelated=false&api_key=519d0af2e2370620f995a280fbb039228c81c5a4eaa0a8e07&includeTags=false&useCanonical=false"\
        .format(urllib2.quote(data))
    req1 = urllib2.Request(subject_one_wiki_url_worknik)
    resp1 = urllib2.urlopen(req1)
    print json.load(resp1)

#    respjson1 = json.load(resp1)
#    print respjson1[0]
#    print respjson1[0]['word']
#    print respjson1[0]['partOfSpeech']
#    print respjson1[0]['text']
#    print respjson1[0]['attributionText']
#    xml1 = resp1.read()
#    soup1 = BeautifulSoup(xml1)
##    print soup1.prettify()
##    print soup1.definition.attributiontext.text
##    print soup1.definition.word.text
#    print soup1.findAll(sequence="0")[0].prettify()
#    print soup1.findAll(sequence="0")[0].word.text
#    print soup1.findAll(sequence="0")[0].attributiontext.text
#    print soup1.findAll(sequence="0")[0].partofspeech.text
#    print soup1.findAll(sequence="0")[0]

get_subject_one_data_wordnik('dog')