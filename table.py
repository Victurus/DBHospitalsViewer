#!C:\Python36\python.exe

import pyodbc

class DBHelper(object):
	""" DBHelper позволяет получить доступ к базе данных """
	def __init__(self, driver, server, database, uid, pwd, tables, views):
		self.connector = pyodbc.connect("DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;" % (driver, server, database, uid, pwd), autocommit=False)
		self.tables = tables
		self.views = views

	def set_cursor(self):
		self.cursor = self.connector.cursor()

	def select_query(self, from_tablename, fields = ["*"], where_rules = "", join_rules = ""):
		tb    = from_tablename
		flds  = ','.join([self.clean_value(val, '[*]\'') for val in fields])
		whrls = where_rules
		jnrls = join_rules
		query = "SELECT %s FROM %s " % (flds, tb)
		if whrls != "":
			query += " WHERE %s " % (whrls)
		if jnrls != "":
			query += jnrls
		rows = [[]]
		self.cursor.execute(query)
		for item in self.cursor.description:
			rows[0] += [item[0]]
		rows += self.cursor.fetchall()
		return rows

	def insert_query(self, to_tablename, values):
		tbn = self.check_tblname(to_tablename)
		if tbn != "":
			query = "INSERT INTO %s VALUES " % (tbn.upper())
			cleanvalues = ""
			for item in values:
				if item.isdigit():
					cleanvalues += "%s," % (self.clean_value(item, '- '))
				else:
					cleanvalues += "N'%s'," % (self.clean_value(item, '- '))
			cleanvalues = "(%s)" % (cleanvalues[0:-1])
			query += cleanvalues
			self.cursor.execute(query)
			self.commit()
			return "Data inserted"
		else:
			return "Error: table name not found"

	def delete_query(self, from_tablename, where_rule):
		tbn = self.check_tblname(from_tablename)
		if tbn != "":
			query = "DELETE FROM %s " % (tbn)
			if where_rule != "":
				new_rule = "WHERE %s" % (where_rule)
				self.cursor.execute(query + new_rule)
				self.commit()
			return "Data deleted"
		else:
			return "Error: table name not found"

	def get_description(self, tablename):
		query = "SELECT * FROM  %s" % (tablename)
		self.cursor.execute(query)
		row = []
		for item in self.cursor.description:
			row.append(item[0])
		return row

	def get_table_rows(self, tablename):
		query = "SELECT * FROM  %s" % (tablename)
		self.cursor.execute(query)
		rows = [[]]
		for item in self.cursor.description:
			rows[0] += [item[0]]
		rows += self.cursor.fetchall()
		return rows

	def commit(self):
		self.connector.commit()
	
	def check_tblname(self, tablename):
		curtable = ""
		for item in self.tables:
			if item[0] == tablename:
				curtable = tablename
		for item in self.views:
			if item[0] == tablename:
				curtable = tablename
		return curtable

	def clean_value(self, value, allowsymbols):
		newvalue = ""
		rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
		for symb in value:
			if symb.isalpha() or symb.isdigit() or symb in allowsymbols or symb in rus_alphabet:
				newvalue += symb
		return newvalue

	def clean_query(self, query):
		stop_words = ['drop', '*', '/', '<']
		for item in stop_words:
			query.replace(item, '')