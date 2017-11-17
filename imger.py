#!/usr/bin/env python
# coding=utf-8
import sys
import re
import os
import multiprocessing
dir = "img/"
def download(url):
    print url
    os.popen('wget -P %s %s'% (dir, url))
    
def parse(html):
    f = open(html)
    for line in f:
        match = re.findall(r"https:(.+?)jpg", line)

        #match = re.search("https:(.+?)jpg", line).group(1)
        match1 = re.findall(r"http:(.+?)jpg", line)

        for i in match:
            url = "https:" + i + "jpg"
            process = multiprocessing.Process(target=download,args=(url,))
            process.start()

        for i in match1:
            url = "http:" + i + "jpg"
            process = multiprocessing.Process(target=download,args=(url,))
            process.start()

def basename(url):
    i = url.rindex('/')
    return url[i+1:]

if __name__ == '__main__':
    print "start"
    #html = sys.argv[1]
    url = sys.argv[1]
    os.popen('wget ' + url)
    
    html = basename(url)
    
    #os.popen('mkdir -p '+ html)
    print html
    parse(html)
