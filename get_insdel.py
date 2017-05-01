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

if 'access' in form and 'tableindex' in form:
	access = form.getvalue('access')
	tableindex = int(form.getvalue('tableindex'))
	result = get_ins_del(tableindex, access)

print(header, result, sep='\n')