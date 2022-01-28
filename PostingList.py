import math

from Modules import *
class PostingList:
    num0fDocsThatContainCurrentTerm = -1
    docIdFtdPairs = (Ftd_DocIdPair() for _ in range(num0fDocsThatContainCurrentTerm))
    idft = math.log(1 + (Collection.getNumberOfDocuments() / num0fDocsThatContainCurrentTerm))

    def __init__(self):
        pass


    def getNumberOfDocsThatContainCurrentTerm(self):
        self.num0fDocsThatContainCurrentTerm = len(self.docIdFtdPairs)
        return self.num0fDocsThatContainCurrentWord

    def getDocIdFtdpairs(self):
        return self.docIdFtdPairs

    def getIdft(self):
        return self.idft

    def getFtdFromTheDocIdFtdPairsByDocumentId(self, documentID):
        for pair in self.docIdFtdPairs:
            if(pair.getDocID() == documentID):
                return pair.getTermAppsInDoc()

        ##if the documentID doies not exist in the postingList return -1
        return -1





