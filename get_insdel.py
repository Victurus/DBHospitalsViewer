#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

header = "Content-type: text/html"
result = ""

access = ''
tableindex = -1

if 'access' in form and 'tableindex' in form and 'is_tables' in form:
	access = form.getvalue('access')
	tableindex = int(form.getvalue('tableindex'))
	is_tables = int(form.getvalue('is_tables'))
	result = get_ins_del(tableindex, access, is_tables)

print(header, result, sep='\n')