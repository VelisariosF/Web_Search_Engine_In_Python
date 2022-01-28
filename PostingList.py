import math

from Modules import *
import Collection
class PostingList:
    num0fDocsThatContainCurrentTerm = -1
    ## dictionary in the form of (docId, ftd) pairs
    docIdFtdPairs = {}
    termPosInLexicon = -1
    def __init__(self):
        pass


    def getNumberOfDocsThatContainCurrentTerm(self):
        self.num0fDocsThatContainCurrentTerm = len(self.docIdFtdPairs)
        return self.num0fDocsThatContainCurrentWord

    def getDocIdFtdpairs(self):
        return self.docIdFtdPairs





    def getFtdFromTheDocIdFtdPairsByDocumentId(self, documentID):
         if(not(self.docIdFtdPairs.get(documentID) == None)):
            return self.docIdFtdPairs.get(documentID)

        ##if the documentID doies not exist in the postingList return -1
         return -1

    def getTermPosInLexicon(self):
        return self.termPosInLexicon


