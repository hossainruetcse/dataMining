import codecs
import requests
from bs4 import BeautifulSoup

url="https://www.thehunt.com/celebrities?page="
file=codecs.open("a.txt","w","utf-8")
def crawl_url(url,page):
    #print(page)
    response=requests.get(url+str(page),headers={'Accept':'application/json'})
    items=response.json()['items']
    for item in items:
        #print(item['display_name'])
        file.write(str(item['display_name'])+"  "+item['url']+"\n")



for i in range(1,8):
    crawl_url(url,i)
