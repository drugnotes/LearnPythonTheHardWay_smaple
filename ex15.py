#!/usr/bin/python
# -*- coding: utf-8 -*-

# ʹ��from...import ����ģ��
from sys import argv

# ��scritpt,filenameָ��argv
script, filename = argv

# ���ļ�
txt = open(filename)

print "Here's your file %r:" % filename
# ��ȡ�ĵ�
print txt.read()

# �ٴδ��ĵ�
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open (file_again)
# �ٴζ�д�ĵ�
print txt_again.read()