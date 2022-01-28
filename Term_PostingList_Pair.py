from Modules import *

class Term_PostingList_Pair:


    def __init__(self, term ,postingList):
        self.term = term
        self.postingList = PostingList(postingList)


    def getTermsPostingList(self):
        return self.postingList

    def getTerm(self):
        return self.term

