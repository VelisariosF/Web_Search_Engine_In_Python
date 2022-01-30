
import hmac
import re

import FilesHelper
import HtmlLink
from urllib.request import urlopen
from bs4 import BeautifulSoup

import Tokenizer


class Crawler:
    documentID = 0
    def __init__(self, url_to_crawl, number_of_urls_to_crawl):
        self.url_to_crawl = url_to_crawl
        self.crawled_urls = []
        ##self.crawled_html_links = []
        self.number_of_urls_to_crawl = number_of_urls_to_crawl
        self.stop = False
    
    def start_crawling(self):
      
      html = urlopen(self.url_to_crawl).read()
      urls_found = []
      soup = BeautifulSoup(html, features="html.parser")
      url_text_List = []
      
      while self.stop == False:
        ##if url has not been found before start parsing it
        if(not(self.url_found_before(self.url_to_crawl))):
            for url in soup.find_all('a', attrs={'href': re.compile("^http://")}):
               urls_found.append(url.get('href'))
            url_title = ""
            for title in soup.find_all('title'):
               url_title = title.get_text()
            for text in soup.find_all('p'):
                url_text_List.append(text.getText())
            url_text = Tokenizer.Tokenizer().listToString(url_text_List)

           ## html_link = HtmlLink(url_title, self.url_to_crawl)
           ## self.crawled_html_links.append(html_link)
            self.crawled_urls.append(self.url_to_crawl)
            FilesHelper.FilesHelper().saveDocumentToFile(self.documentID, url_text)
            self.documentID = self.documentID + 1
            url_text_List.clear()
            if(len(self.crawled_urls) == self.number_of_urls_to_crawl):
               self.stop = True
        else:
            ##if url has been found before move to the next url
            self.url_to_crawl = urls_found.pop(0)

    def get_crawled_urls(self):
        return self.crawled_urls


    def url_found_before(self, url):
        for crawled_url in self.crawled_urls:
            if(url == crawled_url):
                return True
        return False

    
              
    
      
        
          






