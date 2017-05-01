#!C:\Python36\python.exe

import pyodbc 

print("Content-type: text/html")
print()
print("""
<html>
<head>
	<title>TEST PAGE</title>
	
	<style type="text/css">
		div
		{
			box-sizing: border-box;
			width: 90%;
			background-color: blue;
			margin:5px;
			padding:20px;
			border-radius: 15%;
		}
	</style>
</head>
<body>

	""")

cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=ASUS;DATABASE=Hospitals;UID=victor;PWD=tir;')
cnxn.setencoding(encoding='utf-8')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM get_dependencies WHERE TABLETO = 'otdel'")

desc = []
for item in cursor.description:
	desc += [item[0]]

data = cursor.fetchall()

for row in data:
	print("<div>")
	for i in range(len(desc)):
		print(desc[i], ":", row[i], "<br>")
	print("</div>")

print("""
	\n
	</body>
</html>
	""")
# while row:
#     # print(*row)
#     print("<p>", end='')
#     for item in row:
#     	print(" %*s " % (10, str(item)), end='')
#     print("</p>")
#     row = cursor.fetchone()
