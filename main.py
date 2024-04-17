import json
import requests
import os
from bs4 import BeautifulSoup as bs

class Html_downloader():
    def __init__(self) -> None:
        url_list_file = "solutions_urls.json"
        self.main_urls = self.read_urls(url_list_file)

    def read_urls(self,filename) -> dict:
        with open(filename, 'r') as r:
            urls = json.load(r)
        return urls

    def download_html(self, url, save_path) -> None:
        r = requests.get(url, allow_redirects=True)
        with open(save_path,'wb') as f:
            f.write(r.content)

    def download_main_htmls(self) -> None:
        for name,url in self.main_urls.items():
            filename = 'main.html'
            path = f'./cache/html/{name}/'
            if not os.path.exists(path):
                os.mkdir(path)
            full_path = path + filename
            self.download_html(url,full_path)

def load_html(filename):
    with open(filename, 'r') as f:
        return f.read()

def parse_html(filename):
    target = load_html(filename)
    html = bs(target, 'html.parser')
    return html

def parse_cbsol_single_pages():
    html_main = './cache/html/cbsol/main.html'
    html  = parse_html(html_main)
    raw_links = html.find_all('a', class_='relative')[3:]
    clean_links = [link.attrs['href'] for link in raw_links]
    return clean_links

if __name__ == '__main__':
    # htmls = Html_downloader()
    # htmls.download_main_htmls()
    # soup = scrape_single_pages()
    # print(soup.find_all(class_="relative"))
    # for x in soup.find_all(class_="relative")[:3]:
    # for x in soup.find_all('a', class_='relative')[3:]:
    #     print(x.attrs['href'])
    # print(soup.find_all('a')[:10])
    print(parse_cbsol_single_pages())