import FilesHelper
from Modules import *


class Tokenizer:

    def __init__(self):
        self.stopWordSet = FilesHelper.FilesHelper().getStopWordsFromFileAsAList()

    def tokenizeQuery(self, query):
        ##tokenize the query
        tokenizedQuery = ""
        ##write your code here

        return tokenizedQuery

    ## method to tokenize the html text
    def tokenizeHmtlText(self, text):
        ##1st remove stop words
        newText = self.removeStopWords(text)
        ##2nd remove punctuation
        newText2 = self.removePunctuation(newText)

        ##3rd convert all terms to lower case
        newText3 = self.convertTextToLowercaseTerms(newText2)

        ##4rth stem the terms (lemmatization)
        newText4 = self.stemGivenText(newText3)

        return newText4


    ##method to convert all terms to lower
    def convertTextToLowercaseTerms(self, text):
        return str(text).lower()

    ##method to stem a term
    def stemTheTerm(self, term):
        return PorterStemmer().stem(term)


    ## method to stem the text
    def stemGivenText(self, text):
        terms = list(text.split(" "))
        for term in terms:
            newTerm = self.stemTheTerm(term)
            term = newTerm

        return self.listToString(terms)



    ## method to remove the stopwords from the text
    def removeStopWords(self, text):
        terms = list(text.split(" "))
        stopWordsInGivenText = []
        for term in terms:
            if (self.isStopWord(term)):
                stopWordsInGivenText.append(term)

        for stopWord in stopWordsInGivenText:
            terms.remove(stopWord)
        ## return the given text
        ## but first convert it to  string
        return self.listToString(terms)

    ## method to check if a term is a stopword
    def isStopWord(self, term):
        if term in self.stopWordSet:
            return True
        return False


    ##method to remove the punctuation
    def removePunctuation(self, text):
        return re.sub(r'[^\w\s]', ' ', text)


   ## method to convert a list to a string
    def listToString(self, s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele
            str1 += " "

            # return string
        return str1