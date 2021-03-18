import os
import requests
from bs4 import BeautifulSoup
def create(t,name):
    with open(name,'wb') as file:
        file.write(t.encode())
def get(content,i,s):
    soup = BeautifulSoup(content, 'html.parser')
    for el in soup.find_all('span', class_='c-meta__type', text=s):
        p = 'https://www.nature.com' + el.find_previous('a', {"data-track-action":"view article"}).get('href')
        soup = BeautifulSoup(requests.get(p).content, 'html.parser')
        t = soup.find('div',{"class":["c-article-body","article__body cleared","article-item__body"]}).text.strip()
        name = '{}/{}.txt'.format(f"Page_{i}", el.find_previous('a', {
                "data-track-action": "view article"}).text.strip().replace('.', '').replace('!', '').replace(':','').replace(' ', '_').replace('?', ''))
        create(t,name)
def set(n,s):
    for i in range(1,n+1):
        link = f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={i}'
        content = requests.get(link).content
        os.mkdir(f'Page_{i}/')
        get(content,i,s)
set(int(input()),input())





