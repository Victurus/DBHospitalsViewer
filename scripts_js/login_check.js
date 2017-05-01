function validate(form)
{
	var passed = validateUserName(form) && validateUserPassword(form)
	if(!passed)
		window.stop()
	return passed
}

function validateUserName(form)
{
	var username = form.login.value
	username = username.replace(' ', '')
	var result = ""
	var reg = /[^a-zA-Z0-9_-]/g
	if (username == "")
	{
		result += "Username wasn't entered\n"
	}
	if (reg.test(username))
	{
		result += "Only [a-z A-Z 0-9 _ - ] symbols allowed\n"
	}

	if (result == "")
	{
		form.login.style.background = "#F2F2F2";
		form.login.title = ""
		return true;
	}
	else
	{
		form.login.style.background = "red";
		form.login.title = result
		return false;
	}
}

function validateUserPassword(form)
{
	var userpassword = form.password.value
	userpassword = userpassword.replace(' ', '')
	var result = ""
	if (userpassword == "")
		result += "User password wasn't entered\n"
	if (userpassword.length < 4)
		result += "Password can't be less than 4 characters\n"

	if (result == "")
	{
		form.password.style.background = "#F2F2F2";
		form.password.title = ""
		return true;
	}
	else
	{
		form.password.style.background = "red";
		form.password.title = result
		return false;
	}
}
