import re

from Modules import *
from QueryHelper import QueryHelper


class Query:
     ## terms : list of the query terms
     def __init__(self, terms):
         self.terms = terms
         self.queryVector = []
         self.queryLength = -1

     ## function to calculate the vector of the query
     def calculateQueryVector(self):
         ## get the (term, appearances in query) pairs
         termFtqPairs = dict(QueryHelper.getTermFtqPair(self.terms))
         for i in range(0 ,Collection.getNumberOfTerms()):
             self.queryVector.append(0.0)
         for term in termFtqPairs.keys():
             ## get the term's apps in query
             tftq = termFtqPairs.get(term)
             idft = PostingList(dict(InvertedIndex.getInvertedIndexData()).get(term)).getIdft()
             termPosInLexicon = PostingList(dict(InvertedIndex.getInvertedIndexData()).get(term)).getTermPosInLexicon()
             Wtq = tftq * idft
             self.queryVector[termPosInLexicon] = Wtq


     ##Method to get the vector of the given query
     def getQueryVector(self):
         return self.queryVector

     ## Method to calculate the length of the given query
     def calculateQueryLength(self):
         sum = 0
         for weight in self.queryVector:
             sum = sum + math.pow(weight, 2)
         self.queryLength = math.sqrt(sum)

     ## Methon to get the query's length
     def getQueryLength(self):
         return self.queryLength