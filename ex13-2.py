#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
name = raw_input()
age = raw_input()
school =raw_input()
job = raw_input()
script, name, age, school, job = argv

print "The script is called:", script
print "Your name is:", name
print "Your age is:", age
print "Your school is :", school
print "Your job is:", job
