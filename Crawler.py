
import hmac
import re
import HtmlLink
from urllib.request import urlopen
from bs4 import BeautifulSoup



class Crawler:
    def __init__(self, url_to_crawl, number_of_urls_to_crawl):
        self.url_to_crawl = url_to_crawl
        self.crawled_urls = []
        self.crawled_html_links = []
        self.number_of_urls_to_crawl = number_of_urls_to_crawl
        self.stop = False
    
    def start_crawling(self):
      
      html = urlopen(self.url_to_crawl).read()
      urls_found = []
      soup = BeautifulSoup(html, features="html.parser")
      
      
      while self.stop == False:
        ##if url has not been found before start parsing it
        if(not(self.url_found_before(self.url_to_crawl))):
            for url in soup.find_all('a'):
               urls_found.append(url.get('href'))
            url_title = ""
            for title in soup.find_all('title'):
               url_title = title.get_text()
            html_link = HtmlLink(url_title, self.url_to_crawl)
            self.crawled_html_links.append(html_link)
            self.crawled_urls.append(self.url_to_crawl)
            if(len(self.crawled_urls) == self.number_of_urls_to_crawl):
               self.stop = True
        else:
            ##if url has been found before move to the next url
            self.url_to_crawl = urls_found.pop(0)

    def get_crawled_urls(self):
        return self.crawled_urls
    def get_crawled_urls_titles(self):
        titles = []
        for html_link in self.crawled_html_links:
            titles.append(html_link.get_title())
        return titles

    def url_found_before(self, url):
        for crawled_url in self.crawled_urls:
            if(url == crawled_url):
                return True
        return False

    
              
    
      
        
          







start_url = "https://en.wikipedia.org/wiki/World_War_II"

crawler  = Crawler(start_url, 3)
crawler.start_crawling()

print(crawler.get_crawled_urls_titles())