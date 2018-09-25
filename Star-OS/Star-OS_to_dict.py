#!/usr/bin/env python3
# -*- coding: utf-8

ignore = ['duplex', 'alias', 'Current configuration']

def check_ignore(command, ignore):
	return any(word in command for word in ignore)

def conf_Star_OS_to_dict(filename):
	with open(filename) as file:
		dict3 = {}
		level1 = ''
		level2 = ''
		level3 = ''
		for line in file:
			if line.startswith('!') or check_ignore(line, ignore):
				pass
			elif line.startswith('  ') and line[2].isalpha():
				level1 = line.strip()
				dict3[level1] = {}
			elif line.startswith('    ') and line[4].isalpha():
				level2 = line.strip()
				dict3[level1][level2] = {}
			elif line.startswith('      ') and line[6].isalpha():
				level3 = line.strip()
				dict3[level1][level2][level3] = []
			elif line.startswith('        ') and line[8].isalpha():
				level4 = line.strip()
				dict3[level1][level2][level3].append(level4)
		return dict3
