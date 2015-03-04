#!/usr/bin/python
# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Floriba': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michingan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out more cities
print '-' * 10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

# print some states
print '-' * 10
print "Michingan's abbreviation is:", states['Michingan']
print "Floriba's abbreviation is:", states['Floriba']

# do it by using the state then cities dict
print '-' * 10
print "Michingan has:", cities[states['Michingan']]
print "Floriba has:", cities[states['Floriba']]

# printevery state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# Now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '-' * 10
# safely get a abbreviation by state that mnght not be there
state = states.get('Txtas', None)

if not state:
	print "Sorry, no texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

