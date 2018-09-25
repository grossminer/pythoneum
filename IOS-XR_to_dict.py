#!/usr/bin/env python3
# -*- coding: utf-8

ignore = ['user', 'group', 'full-name', 'hashed-password']

def check_ignore(command, ignore):
	return any(word in command for word in ignore)

def conf_XR_to_dict(filename):
	with open(filename) as file:
		result = {}
		level1 = ''
		level2 = ''
		level3 = ''
	for line in file:
		if line.startswith('!') or check_ignore(line, ignore):
			pass
		elif line[0].isalpha():
			level1 = line.strip()
			result[level1] = {}
		elif line.startswith(' ') and line[1].isalpha():
			level2 = line.strip()
			result[level1][level2] = {}
		elif line.startswith('  ') and line[2].isalpha():
			level3 = line.strip()
			result[level1][level2][level3] = []
		elif line.startswith('   ') and line[3].isalpha():
			level4 = line.strip()
			result[level1][level2][level3].append(level4)
		return result
