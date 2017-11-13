import re, os
from fnmatch import fnmatch

def string_split(line):
	print(line.split())
	print(re.split(r'[;,\s]\s*', line))
	# re capture group
	fileds = re.split(r'(;|,|\s)\s*', line)
	print(fileds)
	print(re.split(r'(?:,|;|\s)\s*', line))

def str_match():
	# str.startswith() and str.endswith() arg must be tuple
	filenames = os.listdir('.')
	c_filename = [name for name in filenames if name.endswith(('.c', '.h'))]
	# one or more python file
	any(name.endswith('.py') for name in filenames)

def wildcard_character():
	fnmatch('foo.txt', '*.txt')
	fnmatch('foo.txt', '?oo.txt')
	fnmatch('Dat45.csv', 'Dat[0-9]*')

if __name__ == '__main__':
	line = 'asdf fjdk; afed, fjek,asdf, foo'
	string_split(line)
	str_match()
	wildcard_character()