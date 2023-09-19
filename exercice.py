#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	list_name = name.split("-")
	first_name = list_name[0]
	capital_name = first_name.capitalize()
	sentence = f"Bonjour {capital_name}"
	return sentence

def get_random_sentence(animals, adjectives, fruits):
	list_animals =[]
	list_adjectives = []
	list_fruits = []
	for being in animals:
		list_animals.append(being)
		random.shuffle(list_animals)
	for words in adjectives:
		list_adjectives.append(words)
		random.shuffle(list_adjectives)
	for food in fruits:
		list_fruits.append(food)
		random.shuffle(list_fruits)
	sentence = f"Aujourd’hui, j’ai vu un {list_animals[0]} s’emparer d’un panier {list_adjectives[0]} plein de {list_fruits[0]}."
	return sentence
	

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
