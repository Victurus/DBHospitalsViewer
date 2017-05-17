#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

tableindex=fcol=ecol=strow=cntrow= -1
access = ""

if 'table' in form and 'access' in form and 'fcol' in form and 'ecol' in form and 'strow' in form and 'cntrow' in form and 'is_tables' in form:
	tableindex = int(form.getvalue('table'))
	access = form.getvalue('access')
	fcol = int(form.getvalue('fcol'))
	ecol = int(form.getvalue('ecol'))
	strow = int(form.getvalue('strow'))
	cntrow = int(form.getvalue('cntrow'))
	is_tables = int(form.getvalue('is_tables'))
	if 'data' in form and 'ids' in form:
		where_rules = form.getvalue('data')
		ids = form.getvalue('ids')
		ids = ids.replace('_search', '')
	else:
		where_rules = ""
		ids = ""

print("Content-type: text/html")
print()

if tableindex != -1:
	print(table_str(tableindex, strow, cntrow, is_tables, fcol, ecol, where_rules=where_rules, ids=ids))
else:
	print("Ошибка: такой таблицы/представления нет!")