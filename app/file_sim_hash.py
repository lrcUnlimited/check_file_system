# -*- coding: utf-8 -*-
__author__ = 'li'

import codecs
from  app import simhash
from app import db

"""
获取文件的hash码
"""


def get_simlar_file(filepath):
    f = codecs.open(filepath, 'r', 'gb2312')
    filecontent = f.read()
    # 当前文件的hash
    filehash = simhash.simhash(filecontent)
    # 获取数据库中的hash值
    dict_hash = db.get_data()
    # 存储文件与数据库hash码的汉明距离
    minfilepath = ''
    min_distance = 64
    for k, v in dict_hash.items():
        distance = filehash.hamming_distance(int(v))
        if (distance < min_distance):
            min_distance = distance
            minfilepath = k
    param = (filepath, filehash)
    db.save_file_hash(param)
    simpercent = 0
    if minfilepath == '':
        simpercent = 0
    else:
        simpercent = filehash.similarity(int(dict_hash[minfilepath]))
    return (minfilepath, filecontent, min_distance, simpercent)










