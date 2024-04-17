import json
import requests
import os
import re
from bs4 import BeautifulSoup as bs

def read_urls() -> dict:
    url_list_file = "solutions_urls.json"
    with open(url_list_file, 'r') as r:
        urls = json.load(r)
    return urls
class Html_downloader():
    def __init__(self) -> None:
        self.main_urls = read_urls()

    def download_html(self, url, save_path) -> None:
        r = requests.get(url, allow_redirects=True)
        soup = bs(r.content, 'html.parser').prettify()
        with open(save_path,'w', encoding='utf-8') as f:
            f.write(soup)
    
    def download_gist(self):
        url = 'https://api.github.com/users/Ullvang/gists'
        path = './cache/cbsol_gists.json'
        r = requests.get(url).json()
        with open(path,'w') as f:
            json.dump(r, f, indent=4)

    def download_main_htmls(self) -> None:
        for name,url in self.main_urls.items():
            filename = 'main.html'
            path = f'./cache/html/{name}/'
            if not os.path.exists(path):
                os.mkdir(path)
            full_path = path + filename
            self.download_html(url,full_path)

    def download_all_singles(self,url_list,limit=0):
        if limit:
            for name in url_list:
                url_list[name] = url_list[name][:limit]
        for name in url_list:
            path = f'./cache/html/{name}/'
            for i,url in enumerate(url_list[name]):
                full_path = path + str(i+1) + '.html'
                self.download_html(url,full_path)
class Html_parser():
    def __init__(self) -> None:
      self.main_urls = read_urls()
      self.single_urls = {}

    def load_html(self,filename):
        with open(filename, 'r') as f:
            return f.read()

    def parse_html(self,filename):
        target = self.load_html(filename)
        html = bs(target, 'html.parser')
        return html
    
    def get_all_single_links(self):
        self.get_single_urls_cbsol()


    def get_single_urls_cbsol(self):
        names = self.get_single_names_cbsol()
    
    def get_single_names_cbsol(self):
        html_main = './cache/html/cbsol/main.html'
        # base_url = self.main_urls['cbsol']
        html  = self.parse_html(html_main)
        raw_links = html.find_all('a', class_='relative')[3:]
        clean_links = [link.attrs['href'] for link in raw_links]
        return clean_links
        # full_links = [base_url+url for url in clean_links]
        # self.single_urls['cbsol'] = full_links

    def single_page_content_cbsol(self):
        full_path = './cache/html/cbsol/1.html'     
        html  = self.parse_html(full_path)
        # print(html.find_all(re.compile('gist')))
        # print(html.prettify())

def read_gist():
    path = './cache/cbsol_gists.json'
    with open(path, 'r') as f:
        gists = json.load(f)
    for gist in gists:
        name = list(gist['files'])[0]
        print(name)
    # print(gists[0]['files'].keys(),gists[0]['files']['raw_url'])
if __name__ == '__main__':
    downloader = Html_downloader()
    # downloader.download_main_htmls()
    # downloader.download_gist()
    parser = Html_parser()
    parser.get_all_single_links()
    # downloader.download_all_singles(parser.single_urls,3)
    parser.single_page_content_cbsol()
    read_gist()