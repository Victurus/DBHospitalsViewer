#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

header = "Content-type: text/html\n"
result = "Nothing happens"

if 'data' in form and 'ids' in form and 'tableindex' in form:
	tableindex = int(form.getvalue('tableindex'))
	data = form.getvalue('data')
	ids = form.getvalue('ids')
	ids = ids.replace('_delete', '')
	result = deleter(tableindex, ids, data)

print(header, result, sep='\n')