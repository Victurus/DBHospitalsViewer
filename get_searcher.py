#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

header = "Content-type: text/html"
result = ""

tableindex = -1

if 'tableindex' in form:
	tableindex = int(form.getvalue('tableindex'))
	result = get_insdelserch(table_names[tableindex][0], 'search')

print(header, result, sep='\n')