import Tokenizer


class FilesHelper:

    def __init__(self):
        pass

    def save_urls_to_file(crawled_urls):
        f = open("crawled_urls.txt", "a")
        for url in crawled_urls:
            f.write(f"{url} \n")
        f.close()

    def getStopWordsFromFileAsAList(self):
        file1 = open('stopwords.txt', 'r', encoding="utf8")
        count = 0
        stopWordsSet = set()
        while True:
            count += 1

            # Get next line from file
            line = file1.readline()

            # if line is empty
            # end of file is reached
            if not line:
                break
            stopWordsSet.add(line.strip())


        file1.close()

        return stopWordsSet

    def saveDocumentToFile(self, documentID, documentText):
        documentFile = open(f'Documents_Collection/{documentID}.txt', 'a', encoding="utf8")
        tokenizedDocumentText = Tokenizer.Tokenizer().tokenizeHmtlText(documentText)
        documentFile.write(tokenizedDocumentText)