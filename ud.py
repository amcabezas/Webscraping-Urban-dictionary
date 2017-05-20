#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

tt = []

def limpiar(sig):
    global limpio
    limpio = sig.replace('\n','')
    tt.append(limpio)

def palabra(word):
    if None == word:
        word = 'ups!'
        print word

    else:
        print word.get_text(),':'

if len(sys.argv) < 2:
    sys.exit()
pal = ' '.join(sys.argv[1:])
url = 'http://www.urbandictionary.com/define.php?term='
url_final = '%s%s' % (url,pal)
web = requests.get(url_final)
status_code = web.status_code
if 200 == status_code:
    html = BeautifulSoup(web.text,'lxml')
    word = html.find('a', class_='word')
    meaning = html.find_all('div', attrs={'class':'meaning'}, limit=3)
    for sig in meaning:
        limpiar(sig.get_text())

    i = 0
    palabra(word)
    if 0 < len(tt):
        while i < len(tt):
            print tt[i].encode('utf-8') 
            i = i + 1
    else:
        pass
