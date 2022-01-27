from Modules import *
class Document:


    def __init__(self, ID, title, text):
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

    def calculateLength(self):


