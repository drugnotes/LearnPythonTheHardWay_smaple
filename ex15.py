#!/usr/bin/python
# -*- coding: utf-8 -*-

# 使用from...import 导入模块
from sys import argv

# 把scritpt,filename指向argv
script, filename = argv

# 打开文件
txt = open(filename)

print "Here's your file %r:" % filename
# 读取文档
print txt.read()

# 再次打开文档
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open (file_again)
# 再次读写文档
print txt_again.read()