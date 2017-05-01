#!C:\Python36\python.exe

import cgi
import cgitb
from dbinfo import *
cgitb.enable()

form = cgi.FieldStorage()

header = "Content-type: text/html"
html = """
<html>
<head>
	<title> Table view </title>
	<link rel="stylesheet" type="text/css" href="styles/tables.css">
	<script type="text/javascript" src="scripts_js/manip_functions.js"></script>
</head>
<body>

<form class="hideform" method="post">
	<input type="hidden" name="who">
</form>

<div id="dependencies">
</div>

<div class="main">
	<div class="left">
		<div class="btntabview">
			<div class="btns">
				<button id="set_view" type="button" onclick="set_view(document)">Представления</button><button id="set_table" type="button" onclick="set_table(document)">Таблицы</button>
			</div>

			<div class="tables">
				%s
			</div>
			<div class="views">
				%s
			</div>
		</div>

		<div id="queries">
		</div>
	</div>

	<div class="right">
		<div id="table">
			%s
		</div>

		<div id="manipulator">
			<div id="insdel">
			</div>

			<div>
				<input id="access"       type="hidden" value="%s">
				<input id="strow"        type="hidden" value="%d">
				<input id="cntrowhidden" type="hidden" value="%d">
				<input id="fcol"         type="hidden" value="%d">
				<input id="ecol"         type="hidden" value="%d">
				<input id="is_tables"    type="hidden" value="%d">
				<input id="tableindex"   type="hidden" value="%d">
			</div>

			<div id="move">
				<input class="pn" id="prevtxt" type="text" disabled=0><input class="pn" id="nexttxt" type="text" disabled=0>
				<button type="button" onclick="prev()"> Назад </button><button type="button" onclick="next()"> Вперёд </button>

				<div>
					Отображаемые строки<input type="text" id="cntrowtxt" value="%d" pattern="^[0-9]+$">
				</div>
				<div>
					<button id="accept" type="button" onclick="accept()"> Применить </button>
				</div>
			</div>
		</div>
	</div>
</div>

</body>
</html>
"""

access = "none"
table = "None"
view = "None"
strow = 0
cntrow = 0
fcol = 0
ecol = 0
message = "У вас нет прав для просмотра этой информации"

if 'who' in form:
	if form['who'].value == 'admin':
		access = "admin"
		strow = 0
		cntrow = 50
		fcol = 0
		ecol = -1
	if form['who'].value == 'user':
		access = "user"
		strow = 0
		cntrow = 50
		fcol = 1
		ecol = -1
	if access != "none":
		table = get_table_views(access, True)  # По-умолчанию открыты таблицы, 
		view  = get_table_views(access, False) # не представления
		message = "Выберите таблицу, которую нужно отобразить"

print(header, html % (table, view, message, access, strow, cntrow + strow, fcol, ecol, True, -1, cntrow), sep='\n')