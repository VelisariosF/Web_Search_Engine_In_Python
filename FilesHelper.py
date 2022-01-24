class FilesHelper:
    def __init__(self):
        pass

    def save_urls_to_file(crawled_urls):
        f = open("crawled_urls.txt", "a")
        for url in crawled_urls:
            f.write(f"{url} \n")
        f.close()