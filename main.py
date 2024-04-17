import json
import requests
import os
# import beutif


class Html_downloader():
    def __init__(self, url_list):
        self.main_urls = self.read_urls(url_list)

    def read_urls(self,filename):
        with open(filename, 'r') as r:
            urls = json.load(r)
        return urls

    def download_html(self, url, save_path):
        # save_path = 'test.html'
        r = requests.get(url, allow_redirects=True)
        with open(save_path,'wb') as f:
            f.write(r.content)

    def download_main_htmls(self):
        urls = self.main_urls
        for name,url in urls.items():
            print(name,url)
            filename = 'main.html'
            path = f'./cache/html/{name}/'
            if not os.path.exists(path):
                os.mkdir(path)
            full_path = path + filename
            self.download_html(url,full_path)

if __name__ == '__main__':
    url_list = "solutions_urls.json"
    htmls = Html_downloader(url_list)
    # htmls.download_main_htmls()
    # urls = read_urls(filename)
    # target_url = urls['cbsol']
    # download_html(target_url)