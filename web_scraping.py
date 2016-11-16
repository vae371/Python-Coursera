import urllib
from BeautifulSoup import *
import re

url ='http://python-data.dr-chuck.net/known_by_Owain.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

for num in range(1,7):
    tags = soup('a')
    tag=tags[17]
    url=tag.get('href')
    #print url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)  
    
tags = soup('a')
tag=tags[17]
print re.search(r'by_(\w*).h',tag.get('href')).group(1)