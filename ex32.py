#!/usr/bin/python
# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#for first kind of for_loop goes through a list
for count in the_count:
	print "This is count %d" % count
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# we can also build lists, first atart with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists undertand
	elements.append(i)
	
# Now we can print them out too
for i in elements:
	print "Element was: %d" % i
	