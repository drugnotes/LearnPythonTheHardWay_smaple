#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class ###(###):":
	  "Make a class named ### that is-a ###.",
	"class ###(object):\n\tdef __init__(self, ***)":
	  "class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self, @@@)":
	  "class ### has-a function named *** that takes self and @@@ parameters.",
	"*** = ###()":
	  "Set *** to an instance of class ###.",
	"***.***(@@@)":
	  "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	  "From *** get the *** attriubute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] =="english":
	PHRASE_FIRST = True
	
# load up the words from the webiste
for word in urlopen(WORD_URL).readline():
	WORDS.append(word.strip())
	
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
				random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_name.append(', '.join(random.sample(WORDS, param_count)))
	
	for sentence in snippet, phrase:
		result = sentence[:]
		
		# fake class names
		for word in class_names:
			result.replace("###", word, 1)
				
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
				
		# fake parameters lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
		