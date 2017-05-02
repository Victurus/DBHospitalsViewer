#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

header = "Content-type: text/html"
result = ""

tableindex = -1

if 'tableindex' in form and 'is_tables' in form and 'access' in form:
	tableindex = int(form.getvalue('tableindex'))
	is_tables = int(form.getvalue('is_tables'))
	access = form.getvalue('access')
	if (is_tables == 1):
		myarray = table_names
	else:
		myarray = views
	result = get_insdelserch(myarray[tableindex][0], 'search', access)

print(header, result, sep='\n')