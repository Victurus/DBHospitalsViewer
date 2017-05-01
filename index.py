#!C:\Python36\python.exe

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
header = "Content-type: text/html"
html = """
<html>
<head>
	<title>Login Hospitals</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="styles/login_page.css">
	<script type="text/javascript" src="scripts_js/login_check.js"></script>
	<script type="text/javascript" src="scripts_js/manip_functions.js"></script>
</head>
<body>

<div class="login_page">
	<div class="left">
		<div class="login_form">
			<div class="form_header"> Login Form </div>
			<form id="main_form" action="index.py" action="post">
				<input type="text"     placeholder="username" name="login"    onkeyup="validateUserName($('main_form'))">
				<input type="password" placeholder="password" name="password" onkeyup="validateUserPassword($('main_form'))">
				<button>login</button>
			</form>
		</div>
	</div>

	<div class="right">
		<div class="info">
			<p>Welcome</p>
			<p>This is login page for Database Hospitals</p>
			%s
		</div>
	</div>
</div>

</body>
</html>
"""

html_login_passed = """
<html>
<head>
	<title> Table view </title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="styles/userarea.css">
	<style type="text/css"> %s </style>
</head>
<body>

<div class="main">
	<div class="left">
		<div class="congrat">
			Welcom, <br>
			%s
		</div>
	</div>

	<div class="middle">
		<div class="info">
			<span> Your Data is: </span>
			<div class="info_data">
				<div class="logpass">
					<div>Login:   </div>
					<div>Password:</div>
				</div>
				<div>
					<input type="text" name="login"    value=%s disabled="0">
					<input type="text" name="password" value=%s disabled="0">
				</div>
			</div>

			<div class="formsender">
				<form action="table_view.py">
					<input type="hidden" name="who" value=%s>
					<input type="submit" name="totable" value="Go to base" autofocus>
				</form>
			</div>
		</div>
	</div>

	<div class="right">
		<div class="time">
			
		</div>
	</div>
</div>

</body>
</html>
"""

if 'login' in form and 'password' in form:
 	if form['login'].value == 'admin' and form['password'].value == 'admin':
 		style = """
 		body
 		{
 			background-image: url(styles/images/admin_background.jpg);
 		}
 		"""
 		html = html_login_passed % (style,'administrator'.upper(), 'admin','admin','admin')
 	elif form['login'].value == 'user' and form['password'].value == 'user':
 		style = """
 		body
 		{
 			background-image: url(styles/images/user_background.jpg);
 		}
 		"""
 		html = html_login_passed % (style, 'user'.upper(), 'user', 'user', 'user')
 	else:
 		html = html % ("<span style='color: yellow;font-family: sans; font-size: 28pt'> Wrong password or login </span>")
else:
	html = html % ("")
 
print(header, html, sep='\n')