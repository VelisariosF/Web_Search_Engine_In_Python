class Ftd_DocIdPair:
    pairID = -1
    termAppsInDoc = -1
    documentID = -1

    def __init__(self, pairID):
        self.pairID = pairID
        self.termAppsInDoc = 0
        self.documentID = -1

    def increaseTermAppsInDoc(self):
        self.termAppsInDoc = self.termAppsInDoc + 1

    def setDocId(self, documentID):
        self.documentID = documentID

    def getPairID(self):
        return self.pairID

    def isItsID(self, pairID):
        if self.pairID == pairID:
            return True
        return False