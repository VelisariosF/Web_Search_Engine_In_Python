import collections
import re

import FilesHelper
from Crawler import Crawler

if __name__ == '__main__':

    '''start_url = "https://en.wikipedia.org/wiki/World_War_II"

    crawler = Crawler(start_url, 5)
    crawler.start_crawling()

    FilesHelper.save_urls_to_file(crawler.get_crawled_urls())
    '''

    str = "helli    am velisarios"

    aa = re.split('\s+', str)

    d = {
        "vel" : 20,
        "mike" : 40,
        "kal" : 15,
        "nik" : 12
    }


    crawler = Crawler("https://en.wikipedia.org/wiki/World_War_II", 3)
    crawler.start_crawling()

