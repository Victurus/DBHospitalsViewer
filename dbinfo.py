#!C:\Python36\python.exe

from table import *

table_names = [
('region'                  , 'Регионы'                     , 'admin') ,
('hospital'                , 'Госпитали'                   , 'admin') ,
('otdel'                   , 'Отделы'                      , 'admin') ,
('specialize'              , 'Специализации'               , 'admin') ,
('room'                    , 'Комнаты'                     , 'admin') ,
('hospital_profession'     , 'Профессии'                   , 'admin') ,
('insurance_org'           , 'Страховые организации'       , 'admin') ,
('doctor'                  , 'Докторы'                     , 'user' ) ,
('doctor_insurance_number' , 'Доктор/Страховщик'           , 'user' ) ,
('patient_personal_info'   , 'Пациент(Персональные данные)', 'user' ) ,
('patient_insurance_number', 'Пациент/Страховщик'          , 'user' ) ,
('operation'               , 'Процедуры'                   , 'user' ) ,
('operation_patient'       , 'Пациент/Процедуры'           , 'user' ) ,
('patient'                 , 'Пациенты'                    , 'user' ) ,
('patient_history'         , 'История болезни'             , 'user' ) 
]

views = [
('doctor_finder', 'Упрощённый поиск докторов', 'none'),
('patients_info', 'Информация о пациентах'   , 'none'),
('VIEW_hospital', 'Справочник госпитали'     , 'admin')
]

Hospitals = DBHelper("ODBC Driver 13 for SQL Server", "ASUS", "Hospitals", "victor", "tir", table_names, views)
Hospitals.set_cursor()

def table_str(index, strow, cntrow, is_tables, fcol=-1, ecol=-1, show_gdependence=True, where_rules=""):
	""" Отображение запроса select таблицей <table> </table> """
	if is_tables:
		rows = Hospitals.select_query(table_names[index][0], where_rules=where_rules)
		realtbname = table_names[index][1]
		if show_gdependence:
			btn_header = '<th> Get dependency </th>'
		else:
			btn_header = ""
	else:
		rows = Hospitals.get_table_rows(views[index][0])
		realtbname = views[index][1]
		btn_header = ''

	result_value = """
	<table> 
		<caption> %s </caption>
		<tr>""" % (realtbname)

	if strow < 0:
		strow = 0
	if cntrow > len(rows) or cntrow < 0:
		cntrow = len(rows) - strow
	if fcol < 0:
		fcol = 0
	if ecol > len(rows[0]) or ecol < 0:
		ecol = len(rows[0])

	result_value += btn_header
	for i in range(fcol, ecol):
		result_value += '<th> %s </th> ' % (rows[0][i])

	result_value += "</tr>\n"

	for row in rows[1 + strow:cntrow + strow + 1]:
		if is_tables and show_gdependence:
			result_value += "<tr><td> <button type='button' onclick='get_dependence(%d, %d, %d)'> get </button> </td>\n" % (index, row[0], is_tables)
		else:
			result_value += "<tr>\n"
		for i in range(fcol, ecol):
			result_value += "<td> %s </td> " % (row[i])
		result_value += "</tr>\n"

	result_value += "</table>"

	return result_value

def get_table_views(access, is_tables):
	""" Вывод имён всех таблиц и задание кнопок для вывода соответствующих таблиц """
	cnt = 0
	if is_tables:
		rowarray = table_names
	else:
		rowarray = views
	tbn = """
	<button type="button" onclick="get_table(%d, '%s', %d)" value="%s">
		%s 
	</button>""" % (cnt, access, is_tables, rowarray[0][0], rowarray[0][1])
	for item in rowarray[1:]:
		cnt += 1
		tbn += """
		<button type="button" onclick="get_table(%d, \'%s\', %d)" value="%s">
			%s 
		</button>\n""" % (cnt, access, is_tables, item[0], item[1])
	return tbn

def get_dependence(tableindex, rowid, access):
	""" Вывод данных дочерних таблиц соответствующих полю родительской таблицы """
	tablename = table_names[tableindex][0]
	tablerealname = table_names[tableindex][1]
	rows = Hospitals.select_query("get_dependencies", where_rules=" TABLETO = '%s'" % tablename)
	result_value = ""
	dependence_query = []
	for row in rows[1:]: # не берём названия полей
		index = -1
		for i in range(len(table_names)):
			if row[0] == table_names[i][0]:
				index = i
				break
		#     				     таблица  поле
		dependence_query.append( (index, row[2]) )

	tables = []
	if access == "full": # отображать id или нет
		fcol = 0
	else:
		fcol = 1
	if dependence_query != []:
		# первая таблица которая будет отображена, остальные - нет
		fst_index = dependence_query[0][0]
		fst_field = dependence_query[0][1]
		result_value += """
		<input id='cur_display' type='hidden' value='%s'>
			<div class='display_btns'>
				<button value='%s' onclick='change_view(this.value)'> 
					%s 
				</button>""" % (table_names[fst_index][0], table_names[fst_index][0], table_names[fst_index][1])

		tables.append("""
			<div id='%s'>
				%s
			</div>""" % (table_names[fst_index][0], table_str(fst_index, 0, -1, 1, fcol, show_gdependence=False, where_rules=" %s = %d " % (fst_field, rowid) ) ) )

		# выборка, запись кнопок
		# t - table; f - field
		for t, f in dependence_query[1:]:
			tbn = table_names[t][0]  # table name
			rtbn = table_names[t][1] # table real name
			result_value += """<button value='%s' onclick='change_view(this.value)'>
									%s 
							   </button>""" % (tbn, rtbn)
			tables.append("""
				<div id='%s' style='display: none;'>
					%s
				</div>
				""" % (tbn, table_str(t, 0, -1, 1, fcol, show_gdependence=False, where_rules=" %s = %d " % (f, rowid) ) ) )
		result_value += "</div>" # закрытие класса кнопок переключения таблиц

		# запись таблиц
		result_value += "<div class='outputtables'>\n"
		for item in tables:
			result_value += item
		result_value += "</div>"
	else:
		result_value = "У %s нет дочерних таблиц" % ( tablename )

	return result_value

def get_ins_del(tableindex, access):
	tablename = table_names[tableindex][0]
	tablerealname = table_names[tableindex][1]
	tableaccess = table_names[tableindex][2]
	if access == tableaccess == 'user':
		print("Доступ user")
	elif access == tableaccess == 'full':
		print("Доступ admin")
	else:
		print("Нет доступа")