#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

if 'tableindex' in form and 'rowid' in form and 'is_tables' in form and 'access' in form:
	tableindex = int(form.getvalue('tableindex'))
	rowid = int(form.getvalue('rowid'))
	is_tables = int(form.getvalue('is_tables'))
	access = form.getvalue('access')
	if is_tables:
		result = get_dependence(tableindex, rowid, access)
	else:
		result = "<div>Views don't have dependencies</div>"

print("Content-type: text/html")
print("")

print("""
	<button id='dependencies_btn' type='button' onclick=' $("dependencies").style.display="none" '> X </button>
	<div id="dependencies_container">
		%s
	</div>
	""" % (result))