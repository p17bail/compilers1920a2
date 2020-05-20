import re

# Callback Function
def cb(m):
	if m.group(0) == '&amp;':
		return '&'
	elif m.group(0) == '&gt;':
		return '>'
	elif m.group(0) == '&lt;':
		return '<'
	elif m.group(0) == '&nbsp;':
		return ' '
   

# Άνοιγμα txt αρχείου
with open('testpage.txt','r') as fp:

	text = fp.read()
        	
	#Εξαγωγή-Εκτύπωση Τίτλου
	rexp = re.compile('<title>(.+?)</title>')
	for m in rexp.finditer(text):
		print(m.group(1))

	#Απαλοιφή Σχολίων
	rexp2 = re.compile('<!--.+?-->',re.DOTALL)
	text = rexp2.sub(" ",text)

	#Διγραφή των tags script και style
	rexp3 = re.compile('<script(.+?)</script>|style=(.+?)',re.DOTALL)
	text = rexp3.sub(" ",text)
 
	#Εξαγωγή και εκτύπωση href
	rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)
	for m2 in rexp4.finditer(text):
		print('{}.{}'.format(m2.group(1),m2.group(2)))

	#Απαλοιφή όλων των Tags
	rexp5 = re.compile('<script>|</script>|<title>|</title>|<!--|-->|<!|>|/>|<html|<head|<meta'
		   	   '|<link|<script|</head|<body|<div|<a|<strong|</strong|<br|</a|</div'
		   	   '|<form|<input|<span|<img|</form|<p|<i|<td|<table|</tr|</table|</span|'
		   	   '<tr|</td|</body|</html|<b|</p|</i|</b|<li|</li|<ul|</ul+')
	text = rexp5.sub(' ',text)

	#Αντικατάσταση των HTML Entities
	rexp6 = re.compile('(&amp;|&gt;|&lt;|&nbsp;)') 
	text = rexp6.sub(cb,text)

	#Μετατροπή των whitespaces
	rexp7 = re.compile('\s+') 
	text = rexp7.sub(' ',text)	
    
    #Εκτύπωση του τροποποιημένου κειμένου
	print(text)
