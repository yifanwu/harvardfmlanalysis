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

def getFML(num):
  
  html_doc = requests.get('http://harvardfml.com/page/'+str(num))
  if v1:
    print html_doc

  soup = BeautifulSoup(html_doc.content)
  
  text = soup.find_all("span", class_="quote")

  if v1:
    print text

  soup_t = BeautifulSoup(str(text))
  cleaned = soup_t.get_text()
  cleaned = cleaned.encode('utf8')
  if v2:
    print cleaned
  
  fml_text_fs = open('/Users/yifanwu/Dev/harvardfmlanalysis/data/fml_text.txt','a')
  fml_text_fs.write(cleaned)

  post_time = soup.find_all("div",class_="datetab")
  
  dictMonth = dict((v,k) for k,v in enumerate(calendar.month_abbr))
  
  time_fs = open('/Users/yifanwu/Dev/harvardfmlanalysis/data/time.txt','a')
  
  for time_line in str(post_time):
    cleaning_time = str(post_time)[22:-14]
    month = cleaning_time[:3]  
    month = dictMonth[month]
    day = cleaning_time[-2:]
    time_fs.write(str(month)+","+str(day)+"\n")

def main():
  if t:
    for x in range(1, 4):
      getFML(x)
  else:
    for x in range(1, 618):
      getFML(x)

main()


