# -*- coding: gb2312  -*-
__author__ = 'li'
import os
import sys
import codecs

from  app import  simhash
f = codecs.open('.././app/static/uploads','r','gb2312')
str=f.read()
print simhash.simhash(str)

f.close()
print(str)
