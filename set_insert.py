#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

header = "Content-type: text/html\n"
result = "Nothing happens"

if 'data' in form and 'tableindex' in form and 'is_tables' in form:
	tableindex = int(form.getvalue('tableindex'))
	data = form.getvalue('data')
	is_tables = form.getvalue('is_tables')
	result = inserter(tableindex, data, is_tables)

print(header, result, sep='\n')