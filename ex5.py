#!/usr/bin/python
# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35 
height = 160
weight = 110
eyes = 'Block'
teeth = 'While'
hair = 'Block'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depenging on the coffee." % teeth

# this line is tricky to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)

# µ¥Î»×ª»»
height_centimeter = height * 2.54  
weight_kilo = weight * 0.4536  
print "He's %d centimeters tall." % height_centimeter  
print "He's %d kilos heavy." % weight_kilo
