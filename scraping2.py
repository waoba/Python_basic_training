import urllib.request
from urllib.parse import urljoin  # URLを扱うモジュールを追加
from bs4 import BeautifulSoup as BS
import os
import csv


class Scraper:
    def __init__(self, site):
        self.site = site
        self.urls = set()  # 収集済みURLを入れておく変数

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BS(html, parser)
        with open("scraping result.csv","w",encoding="utf_8_sig",newline="") as f:
            for tag in sp.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
                if 'atcl/' not in url:  # 'atcl/' を含まないURLは対象外にする
                    continue
                full_url = urljoin(self.site, url)  # ドメイン名を含むURLに変換
                if full_url in self.urls:  # 既に収集済みのURLは対象外にする
                    continue
                self.urls.add(full_url)  # 収集済みURLに追加
                print('\n' + full_url)  # URLを表示
                f.write(full_url.strip()+"\n")
            #w.writerow(self.urls)
        print(self.urls)
        print('\n'+str(len(self.urls))+" news have been found in "+self.site)

news = 'https://www.nikkei.com/technology/'  # ニュース取得元サイトを変更
Scraper(news).scrape()
