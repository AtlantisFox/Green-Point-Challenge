import re
from calendar import month_abbr

if __name__ == '__main__':
	text = 'Today is 11/13/2017. Nari starts 11/09/2017.'
	re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
	datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
	datepat.sub(r'\3-\1-\2', text)
	
	# callback function
	def change_date(m):
		mon_name = month_abbr[int(m.group(1))]
		return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
	datepat.sub(change_date, text)
	newtext, n = datepat.subn(r'\3-\1-\2', text)
	