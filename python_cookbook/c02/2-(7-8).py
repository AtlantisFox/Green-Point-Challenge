# The shortest match and Multi-line matching

import re

def shortest_match():
	text1 = 'shazhao say "no."'
	text2 = 'shazhao say "no." shahua say "yes."'
	str_pat = re.compile(r'\"(.*)\"')
	print(str_pat.findall(text1))
	print(str_pat.findall(text2))
	# shortest match
	str_pat = re.compile(r'\"(.*?)\"')
	print(str_pat.findall(text2))

def multiline_match():
	comment = re.compile(r'/\*(.*?)\*/')
	text1 = '/* this is a comment */'
	text2 = '''/* this is a
	multiline comment */
	'''
	print(comment.findall(text1))
	print(comment.findall(text2))
	# Multi-line matching
	comment = re.compile(r'/\*((?:.|\n)*?)\*/')
	print(comment.findall(text2))
	comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
	print(comment.findall(text2))

if __name__ == '__main__':
	shortest_match()
	multiline_match()
	