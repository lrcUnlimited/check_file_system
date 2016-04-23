# -*- coding: UTF-8 -*-
__author__ = 'li'
"""
利用jieba中文分词组件，对文章的关键词进行抽取
"""
import jieba, codecs
import jieba.analyse

content = codecs.open('static/uploads/woai4.txt', 'r', 'gb2312').read()

tags = jieba.analyse.extract_tags(content, 20, True)


# 获取关键词的hash码
def get_key_hash(v):
    # A variable-length version of Python's builtin hash
    if v == "":
        return 0
    else:
        x = ord(v[0]) << 7
        m = 1000003
        mask = 2 ** 64 - 1
        for c in v:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(v)
        if x == -1:
            x = -2
        return x


fingerprint=bin(get_key_hash('我很乐意将扩大开放空间爱的色放金卡交电费卡积分卡金卡黛珊就付款'))
print len(fingerprint)