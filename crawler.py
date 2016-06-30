#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import bs4
import datetime
import urllib2
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


NEW_LAST_URL=''
TAG_FILE='.last_url'

def find_new_urls(opener):
    global NEW_LAST_URL
    global TAG_FILE

    base_url=u'http://www.sexychinese.net/page/'
    last_url=''

    with open(TAG_FILE) as f:
        last_url=f.readline().strip()
    print last_url
    targets=[]
    for i in range(1,11):
        url=base_url+str(i)
        #print url
        #print opener.open(url).read()
        soup=BeautifulSoup(opener.open(url),'lxml')
        links=soup.find_all("h2",class_="post-title")
        for l in links:
            current_url=l.a['href'].strip()
            if current_url==last_url:
                print '==========FOUND THE LAST ONE==========='
                return targets
            targets.append(current_url)
            NEW_LAST_URL=current_url
    return targets




OUTROOT='./images'

if __name__=='__main__':
    opener=urllib2.build_opener()
    opener.addheaders=[('User-agent', 'Mozilla/5.0')]
    targets=find_new_urls(opener)
    #print NEW_LAST_URL
    #print targets
    

    subdirs=[ int(i) for i in os.listdir(OUTROOT) if '.' not in i]
    subdirs.sort()
    index=subdirs[-1]+1
    print index

    for t in targets:
        if not os.path.exists('%s/%d'%(OUTROOT,index)):
            os.makedirs('%s/%d'%(OUTROOT,index))
        print index,len(targets),'\t',t
        soup=BeautifulSoup(opener.open(t),'lxml')
        print soup.title.string
        f_title=open('%s/%d/title'%(OUTROOT,index),'w')
        f_title.write(soup.title.string)
        f_title.close()

        #tag_div=soup.find("div",class_="post-content")
        tag_div=soup.find("div",class_="entry-inner")
        for tag_img in tag_div.find_all('img'):
            print tag_img["src"]
            url=tag_img['src']
            name=url.split('/')[-1]
            #print name
            img_title=open('%s/%d/%s'%(OUTROOT,index,name),'w')
            try:
                img_title.write(opener.open(url).read())
            except:
                print '[error] at url',url   
            img_title.close()
        #sys.exit(1)
        index+=1

    if len(NEW_LAST_URL)!=0:
        with open(TAG_FILE,'w') as f:
            f.write(NEW_LAST_URL)
