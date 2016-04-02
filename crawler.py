#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import bs4
import datetime
import urllib2
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


BASE_URL=u'http://www.sexychinese.net/tag/%E4%B8%9D%E8%A2%9C/page/'
PAGES=range(1,8)
OUTROOT='./out'

opener=urllib2.build_opener()
opener.addheaders=[('User-agent', 'Mozilla/5.0')]

if __name__=='__main__':
    targets=[]
    for i in PAGES:
        url=BASE_URL+str(i)
        print url
        #print opener.open(url).read()
        soup=BeautifulSoup(opener.open(url),'lxml')
        links=soup.find_all("h2",class_="post-title")
        for l in links:
            #print l.a['href']
            targets.append(l.a['href'])

    index=0
    for t in targets:
        if not os.path.exists('%s/%d'%(OUTROOT,index)):
            os.makedirs('%s/%d'%(OUTROOT,index))
        print t
        soup=BeautifulSoup(opener.open(t),'lxml')
        print soup.title.string
        f_title=open('%s/%d/title'%(OUTROOT,index),'w')
        f_title.write(soup.title.string)
        f_title.close()

        tag_div=soup.find("div",class_="post-content")
        for tag_img in tag_div.find_all('img'):
            print tag_img["src"]
            url=tag_img['src']
            name=url.split('/')[-1]
            #print name
            img_title=open('%s/%d/%s'%(OUTROOT,index,name),'w')
            img_title.write(opener.open(url).read())
            img_title.close()
        #sys.exit(1)
        index+=1
