#!/usr/bin/python
# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crachers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crachers
	print "Man that's enought for a party!"
	print "Get a blanket.\n"
# 把20和30作为cheese_and_crackers的参数	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#把amount_of_cheese和amount_of_cheese作为cheese_and_crackers的两个参数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 直接传入参数，并且通过简单的运算使得参数更加灵活
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"

# 变量amount_of_cheese+100、amount_of_crackers+1000作为函数cheese_and_crackers的参数并且打印出来
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
