class Inverted_Index:
    invertedIndexData = {}
    termDocIdPairs = []
    numberOfDocuments = 0
    documentNames = []
    def __init__(self, rebuildIndex):
        if(rebuildIndex):
            self.invertedIndexData.clear()
        else:
            ##self.invertedIndexData = FilesHelper.loadIndexFromFile()
        self.termDocIdPairs.clear()

        self.firstPass()

        self.termDocIdPairs.clear()

        self.secondPass()

        QueryProcessor.calculateLengthOfDocuments()

        FilesHelper.saveIndexToFile(invertedIndexData)

    def firstPass(self):
        ## 1st read of the collection D.

        for i in range (0, self.numberOfDocuments):
            documentId = i

