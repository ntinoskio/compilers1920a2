import re

with open('testpage.txt','r') as fp:
	text = fp.read()
	q1 = re.compile('<title>(.+?)</title>')
	k = q1.search(text)
	print(k.group(1))
	q2 = re.compile('<!--.*?-->',re.DOTALL)
	text = q2.sub(' ',text)
	q3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL)
	text = q3.sub(' ',text)
	q4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)
	for l in q4.finditer(text):
		print('{} {}'.format(l.group(1),l.group(2)))
	q5 = re.compile(r'<("[^"]*"|\'[^\']*\'|[^\'">])*>',re.DOTALL)
	text = q5.sub(' ',text)
	q6 = re.compile(r'&(nbsp|gt|lt|amp);')
	def cb(m):
		if (m.group(0) == '&nbsp;'):
			return '{}'.format(' ')
		elif (m.group(0) == '&gt;'):
			return '{}'.format('>')
		elif (m.group(0) == '&lt;'):
			return '{}'.format('<')
		elif (m.group(0) == '&amp;'):
			return '{}'.format('&')
	text = q6.sub(cb,text)
	q7 = re.compile(r'\s+')
	text = q7.sub(' ',text)
	print(text)
