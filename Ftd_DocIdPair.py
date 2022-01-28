class Ftd_DocIdPair:
    pairID = -1
    termAppsInDoc = -1
    documentID = -1

    def __init__(self, pairID, docId):
        self.pairID = pairID
        self.termAppsInDoc = 0
        self.documentID = docId

    def increaseTermAppsInDoc(self):
        self.termAppsInDoc = self.termAppsInDoc + 1

    def setDocId(self, documentID):
        self.documentID = documentID

    def getTermAppsInDoc(self):
        return self.termAppsInDoc

    def getDocID(self):
        return self.documentID

    def getPairID(self):
        return self.pairID

    def isItsID(self, pairID):
        if self.pairID == pairID:
            return True
        return False
