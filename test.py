#!/usr/bin/env python
# -*- coding: utf8 -*- 

import requests
from bs4 import BeautifulSoup, SoupStrainer, Comment
import re
from pprint import pprint


def getT():
  r = requests.get('http://harvardfml.com/')
  t = r.text
  t = t.encode('cp1252')
  #t = t.replace('encoding="UTF-8"', 'encoding="iso-8859-1"')
  print t

#getT()

def removeT():
  soup = BeautifulSoup("""
    <big class="quote">“</big> Guys are always more interested in my friends than me, even when my friends are already taken FML 
                            </span>, <span class="quote">
                        """)
  comments = soup.findAll(text=lambda text:isinstance(text, Comment))
  [comment.extract() for comment in comments]
  print soup

#removeT()


def addLine():
  time_fs = open('/Users/yifanwu/Dev/harvardfml/data/time_t2.txt','a')
  time_fs.write("3")

  time_fs2 = open('/Users/yifanwu/Dev/harvardfml/data/time_t2.txt','a')
  time_fs2.write("4")

addLine()

#pprint(dictMonth)
def test():
  html_doc = """
  <div class="post">
    <a href="http://harvardfml.com/post/35447034346/thought-my-crush-was-flirting-but-he-totally-just"><div class="datetab">Nov<span>10</span></div></a>

      <div class="quote">
          
          <div class="caption">
              <span class="tip"></span>
              <span class="quote">
                  <big class="quote">“</big> Thought my crush was flirting, but he totally just wanted a class/homework buddy. FML 
              </span>
          </div>
      </div>
  <br>
  <div style="font-size: 10px; text-align: right;"><a class="dsq-comment-count" href="http://harvardfml.com/post/35447034346/thought-my-crush-was-flirting-but-he-totally-just#disqus_thread">Comments</a></div> 
                      
  """