import math

import HerlperFunctions
from InvertedIndex import InvertedIndex
from Modules import *
from Term_PostingList_Pair import Term_PostingList_Pair


class Document:


    def __init__(self, ID, title):
        self.documentID = ID
        self.documentLENGTH = -1
        self.documentTitle = title
        self.documentVector = []

    def getDocumentTextByID(self, id):
        document = open(f"{id}.txt", "r")
        return document.readlines()

    def getDocID(self):
        return self.documentID

    def getDocTitle(self):
        return self.documentTitle

    ##method to calculate the vector of a specfic document
    def calculateDocumentVector(self, documentId):
        ## get the data form the index
        invertedIndexData = dict(InvertedIndex.getInvertedIndexData())
        for term in invertedIndexData.keys():
            ##for every (term, postingList) pair get the posting list
            postingList = invertedIndexData.get(term)
            ##fom the terms posting list get the ftd of this specific doc using the docs Id
            ftd = postingList.getFtdFromTheDocIdFtdPairsByDocumentId(documentID)
            if(ftd != -1):
                ## if ftd is not equal to -1 it means this term exists in the specific document
                ## thus we can calculate its weight in the specific document
               tftd = 1 + math.log(ftd, math.e)
               idft = postingList.getIdft()
               Wtd = tftd * idft
               self.documentVector.append(Wtd)
            else:

                ## if ftd == -1 it means this term does not exist in this doc so in that position of the vector
                ## we insert 0.0
                self.documentVector.append(0.0)


    def calculateLengthOfDocument(self):
        sum = 0
        for weight in self.documentVector:
            sum = sum + math.pow(weight, 2)
        self.documentLENGTH = math.sqrt(sum)


    def getDocumentLenth(self):
        return self.documentLENGTH






