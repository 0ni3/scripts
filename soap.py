import requests
import sys
from bs4 import BeautifulSoup, Comment
import re, htmlentitydefs
from HTMLParser import HTMLParseError
from datetime import datetime
import subprocess
import os
import urllib2

#if __name__ == "__main__":
page = requests.get(sys.argv[1])
soup = BeautifulSoup(page.content, 'html.parser')
text = soup.select('div.docsity-document-extract__content__page')
#bs2 = BeautifulSoup(text)

for t in text[0:5]:
    print(t)
#page =requests.get("https://www.docsity.com/it/appunti-completi-filologia-germanica-guerrieri-modulo-b-a-a-2016-2017/2174379/")
