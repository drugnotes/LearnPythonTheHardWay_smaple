#!/usr/bin/python
# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crachers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crachers
	print "Man that's enought for a party!"
	print "Get a blanket.\n"
# ��20��30��Ϊcheese_and_crackers�Ĳ���	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#��amount_of_cheese��amount_of_cheese��Ϊcheese_and_crackers����������
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# ֱ�Ӵ������������ͨ���򵥵�����ʹ�ò����������
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"

# ����amount_of_cheese+100��amount_of_crackers+1000��Ϊ����cheese_and_crackers�Ĳ������Ҵ�ӡ����
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
