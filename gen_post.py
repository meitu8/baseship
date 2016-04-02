#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

IMAGE_ROOT='./images'
POST_ROOT='./_posts'


names=os.listdir(IMAGE_ROOT)

for x in names:
    if '.' in x:
        continue
    title=open('%s/%s/title'%(IMAGE_ROOT,x)).read().strip()
    if ']' in title:
        title=title.split(']')[-1]
    if '|' in title:
        title=title.split('|')[0]
    f_post=open('%s/%s.md'%(POST_ROOT,x),'w')
    f_post.write('---\n')
    f_post.write('title: %s\n'%title)
    f_post.write('---\n')

    pics=os.listdir('%s/%s'%(IMAGE_ROOT,x))
    pics.sort()
    for pic in pics:
        if 'title' in pic or '.' == pic[0]:
            continue
        f_post.write(u'![](/%s/%s/%s)\n'%(IMAGE_ROOT,x,pic))

