import re

datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)


# capture group

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/13/2017')
print(m.group(0), m.group(1), m.group(2), m.group(3), m.groups())
datepat.findall(text)
for m in datepat.finditer(text):
	print(m.groups)