import math

from Modules import *

class QueryProcessor:
    documentsAccumulators = {}
    documentsLenghts = {}
    def __init__(self):
        pass


    def intializeDocumentLenghts(self):
        for docId in range(0 , Collection.getNumberOfDocuments):
            self.documentsLenghts[docId] = Document.g
    def topKInverted(self, query):
        queryTerms = QueryHelper.getQueryTerms(query)
        lexicon = dict(InvertedIndex.getInvertedIndexData())
        for term in queryTerms:
            termsPostingList = PostingList(lexicon.get(term))
            nt = termsPostingList.getNumberOfDocsThatContainCurrentTerm()
            idft = math.log((1 + (Collection.getNumberOfDocuments() / nt)), math.e)
            termsPostingListPairs = dict(termsPostingList.getDocIdFtdpairs())
            for docId in termsPostingListPairs.keys():
                ## if the accumulator of this document does not exist the create it
                if(self.documentsAccumulators.get(docId) == None):
                    self.documentsAccumulators[docId] = 0.0

                ftd = termsPostingListPairs.get(docId)
                tftd = 1 + math.log(ftd, math.e)
                Wtd = tftd*idft
                ##update the accumulator by adding the weight
                previousSum = self.documentsAccumulators.get(docId)
                newSum = previousSum + Wtd
                ##
                self.documentsAccumulators.update({docId : newSum})

        for i in range(0, Collection.getNumberOfDocuments()):
            previousResult = self.documentsAccumulators.get(docId)
            newResult = previousResult /






