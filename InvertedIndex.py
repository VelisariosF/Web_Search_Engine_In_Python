from Modules import *
from Term_PostingList_Pair import Term_PostingList_Pair


class InvertedIndex:
   data = [Term_PostingList_Pair() for _ in range(Collection.getNumberOfTerms())]
   def __init__(self):
       pass

   def getInvertedIndexData(self):
       return self.data

