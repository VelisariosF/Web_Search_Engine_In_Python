import re

from Modules import *

class QueryHelper:
    def __init__(self):
        pass


    def checkIfKeyExists(self, givenKey, dictionary):
        for key in dictionary.keys():
            if givenKey == key:
                return True
        return False

    def getTermFtqPair(self, listOfQueryTerms):
        pairs = {}
        for term in listOfQueryTerms:
            if(not(self.checkIfKeyExists(term, listOfQueryTerms))):
                pairs[term] = 1
            else:
                apps = pairs.get(term)
                pairs.update({term : apps + 1})

        return pairs

    ##methon to get Terms idft from the inverted index
    def getIdft(self, term):
        pass
        ##data = (Term_PostingList_Pair)InvertedIndex.getInvertedIndexData()
        ##for term

    ##get the terms of the tokenized query as a list
    def getQueryTerms(self, query):
        return re.split("\\s+", Tokenizer.tokenizeQuery(query))
