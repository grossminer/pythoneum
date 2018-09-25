#!/usr/bin/env python3
# -*- coding: utf-8

ignore = ['user', 'group', 'full-name', 'hashed-password']

def check_ignore(command, ignore):
	return any(word in command for word in ignore)

def conftodict(filename):
	with open(filename) as file:
		result = {}
		level0 = ''
		level1 = ''
		level2 = ''
		for line in file:
			if line.startswith('!') or check_ignore(line, ignore):
				pass
			elif line[0].isalpha():
				level0 = line.strip()
				result[level0] = {}
			elif line.startswith('  ') and (line[2].isalpha() or line[2].isdigit()):
				level1 = line.strip()
				result[level0][level1] = {}
			elif line.startswith('    ') and line[4].isalpha():
				level2 = line.strip()
				result[level0][level1][level2] = []
			elif line.startswith('      ') and line[6].isalpha():
				result[level0][level1][level2].append(line.strip())
		return result
