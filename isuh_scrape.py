#!/usr/bin/env python
# -*- coding: utf8 -*- 
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
from pprint import pprint
import calendar


#macro
v1 = False
v2 = False
t = False

def getISU(num):
  
  html_doc = requests.get('http://isawyouharvard.com/index.php?page='+str(num))
  if v1:
    print html_doc

  soup = BeautifulSoup(html_doc.content)
  
  text = soup.find_all("div", class_="post")

  soup_t = BeautifulSoup(str(text))
  cleaned = soup_t.get_text()
  cleaned = cleaned.encode('utf8')

  if v1:
    print cleaned

  fml_text_fs = open('/Users/yifanwu/Dropbox/Dev/harvardfmlanalysis/data/isu_text.txt','a')
  fml_text_fs.write(cleaned)

def main():
  if t:
    for x in range(1, 4):
      getISU(x)
  else:
    for x in range(1, 1943):
      getISU(x)  
  

main()