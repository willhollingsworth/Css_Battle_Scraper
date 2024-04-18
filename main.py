import json
import requests
import os
import re
import shutil
from bs4 import BeautifulSoup as bs

'''
CSS Battle Scraper
'''

def clear_cache():
    cache = './cache'
    if os.path.exists(cache):
        shutil.rmtree(cache)

def read_urls() -> dict:
    url_list_file = "solutions_urls.json"
    with open(url_list_file, 'r') as r:
        urls = json.load(r)
    return urls
class Main_downloader():
    def __init__(self) -> None:
        self.contents_urls = read_urls()
        self.required_folders = ['./cache','./cache/html/','./cache/json/']
        self.create_all_required_folders()

    def main(self):
        self.download_all_contents_files()

    def download_all_contents_files(self):
        for name,url in self.contents_urls.items():    
            data = self.download_data(url)
            if self.check_type(name,data) == 'html':
                self.download_contents_html(name,data)
            else :
                self.download_contents_json(name,data)

    def check_type(self,name,data):
        '''TODO: check actual contents of the data and confirm if it's html or json'''
        if name == 'cbsol':
            return 'html'

    def download_data(self,url):
        data = requests.get(url, allow_redirects=True)
        return data
    
    def download_gist(self): 
        url = 'https://api.github.com/users/Ullvang/gists'
        path = './cache/cbsol_gists.json'
        r = requests.get(url).json()
        with open(path,'w') as f:
            json.dump(r, f, indent=4)

    def download_contents_json(self,name,data) -> None:
        filename = 'contents.json'
        path = f'./cache/json/{name}/'
        full_path = path + filename
        self.save_json(data,full_path)

    def download_contents_html(self,name,data) -> None:
        filename = 'contents.html'
        path = f'./cache/html/{name}/'
        full_path = path + filename
        self.save_html(data,full_path)

    def save_html(self, data, save_path) -> None:
        soup = bs(data.content, 'html.parser').prettify()
        with open(save_path,'w', encoding='utf-8') as f:
            f.write(soup)

    def save_json(self, data, save_path) -> None:
        json_data = data.json()
        with open(save_path,'w') as f:
            json.dump(json_data, f, indent=4)

    def download_all_singles(self,url_list,limit=0):
        if limit:  # if limit is set limit each sublist to specified value
            for name in url_list:
                url_list[name] = url_list[name][:limit]
        for name in url_list:
            path = f'./cache/html/{name}/'
            for i,url in enumerate(url_list[name]):
                full_path = path + str(i+1) + '.html'
                self.save_html(url,full_path)

    def create_all_required_folders(self):
        ''' could be more elegant and only create required folders'''
        for folder in self.required_folders:
            if not os.path.exists(folder):
                os.mkdir(folder)
            if folder == './cache' : # dont create subfolder on root folder
                continue      
            for name in self.contents_urls.keys():
                sub_folder =  f'{folder}/{name}/'
                if not os.path.exists(sub_folder):
                    os.mkdir(sub_folder)

class Main_parser():
    def __init__(self) -> None:
      self.contents_urls = read_urls()
      self.single_urls = {}

    def load_html(self,filename):
        with open(filename, 'r') as f:
            return f.read()

    def parse_html(self,filename):
        target = self.load_html(filename)
        html = bs(target, 'html.parser')
        return html
    
    def get_all_single_links(self):
        # self.get_single_urls_cbsol()
        self.get_get_single_urls_automedon()
        pass

    def get_single_names_automedon(self):
        html_contents = './cache/html/automedon/contents.html'
        html  = self.parse_html(html_contents)

    def  get_get_single_urls_automedon(self):
        names = self.get_single_names_cbsol()

    def get_single_urls_cbsol(self):
        # names = self.get_single_names_cbsol()
        pass
    
    def get_single_names_cbsol(self):
        html_contents = './cache/html/cbsol/contents.html'
        # base_url = self.main_urls['cbsol']
        html  = self.parse_html(html_contents)
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

    def read_gist(self):
        path = './cache/cbsol_gists.json'
        with open(path, 'r') as f:
            gists = json.load(f)
        for gist in gists:
            name = list(gist['files'])[0]
            print(name)
        # print(gists[0]['files'].keys(),gists[0]['files']['raw_url'])

if __name__ == '__main__':
    clear_cache()
    downloader = Main_downloader()
    downloader.main()
    downloader.download_all_contents_files()
    # downloader.download_gist()
    # parser = Main_parser()
    # parser.get_all_single_links()
    # downloader.download_all_singles(parser.single_urls,3)
    # parser.single_page_content_cbsol()
    # read_gist()