#!/usr/bin/python
# -*- coding: utf-8 -*-

# 定义cars的指向
cars = 100

# 定义space_in_a_car的指向
space_in_a_car = 4.0

# 定义drivers的指向
drivers = 30

# 定义passengers的指向
passengers = 90

# 没有人开的车=车的数量-司机的数量
cars_not_driven = cars - drivers

# 有人开的车=司机的数量
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
