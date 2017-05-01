function set_view(doc) 
{
	doc.getElementsByClassName('tables')[0].style.display= "none"
	doc.getElementsByClassName('views')[0].style.display= "block"
	$('is_tables').value = 0
}

function set_table(doc) 
{
	doc.getElementsByClassName('views')[0].style.display= "none"
	doc.getElementsByClassName('tables')[0].style.display= "block"
	$('is_tables').value = 1
}

function get_content(params, method, url, fill_id)
{
	// example params
	// params = "url=amazon.com/gp/aw "
	var request = new ajaxRequest()

	request.open("POST", url, true)
	request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
	request.setRequestHeader("Content-length", params.length)
	request.setRequestHeader("Connection", "close")

	request.onreadystatechange = function()
	{
		if (this.readyState == 4)
		{
			if (this.status == 200)
			{
				if (this.responseText != null)
				{
					document.getElementById(fill_id).innerHTML = this.responseText
				}
				else
					alert("Ошибка AJAX: Данные не получены")
			}
			else
				alert("Ошибка AJAX: " + this.statusText)
		}
	}

	request.send(params)
}

function set_content(params, method, url)
{
	var request = new ajaxRequest()

	request.open("POST", url, true)
	request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
	request.setRequestHeader("Content-length", params.length)
	request.setRequestHeader("Connection", "close")

	request.onreadystatechange = function()
	{
		if (this.readyState == 4)
		{
			if (this.status == 200)
			{
				if (this.responseText != null)
				{
					alert(`Результат запроса: ${this.responseText}`)
				}
				else
					alert("Ошибка AJAX: Данные не получены")
			}
			else
				alert("Ошибка AJAX: " + this.statusText)
		}
	}

	request.send(params)
}

function ajaxRequest()
{
	try
	{
		var request = new XMLHttpRequest()
	}
	catch(el)
	{
		try
		{
			request = new ActiveXObject("Msxml2.XMLHTTP")
		}
		catch(e2)
		{
			try
			{
				request = new ActiveXObject("Microsoft.XMLHTTP")
			}
			catch(e3)
			{
				request = false
			}
		}
	}
	return request
}

function $(id)
{

	return document.getElementById(id)
}

function accept()
{
	var tableindex = $('tableindex').value

	if (tableindex != -1)
	{
		var is_tables = $('is_tables').value
		var access = $('access').value
		var cntrow = parseInt($('cntrowtxt').value, 10)
		$('cntrowhidden').value = cntrow
		var fcol = $('fcol').value
		var ecol = $('ecol').value
		var strow = parseInt($('strow').value, 10)

		var query = `table=${tableindex}&access=${access}&fcol=${fcol}&ecol=${ecol}&strow=${strow}&cntrow=${cntrow}&is_tables=${is_tables}`
		get_content(query, 'POST', 'get_table.py', 'table')

		$('prevtxt').value = strow
		$('nexttxt').value = strow + cntrow
	}
}

function get_table(tableindex, access, is_tables)
{
	$('tableindex').value = tableindex
	var fcol = $('fcol').value
	var ecol = $('ecol').value
	var strow = parseInt($('strow').value, 10)
	var cntrow = parseInt($('cntrowhidden').value , 10)

	var query = `table=${tableindex}&access=${access}&fcol=${fcol}&ecol=${ecol}&strow=${strow}&cntrow=${cntrow}&is_tables=${is_tables}`
	get_content(query, 'POST', 'get_table.py', 'table')

	$('prevtxt').value = strow
	$('nexttxt').value = strow + cntrow

	query = `tableindex=${tableindex}&access=${access}`
	get_content(query, 'POST', 'get_insdel.py', 'insdel')
	query = `tableindex=${tableindex}`
	get_content(query, 'POST', 'get_searcher.py', 'queries')
}

function prev()
{
	var tableindex = $('tableindex').value
	if (tableindex != -1)
	{
		var is_tables = $('is_tables').value
		var access = $('access').value
		var cntrow = parseInt($('cntrowhidden').value, 10)
		var strow = parseInt($('strow').value, 10)
		strow -= cntrow
			if(strow < 0)
			{
				$('strow').value = 0
				strow = 0
			}
			else
				$('strow').value = strow
		var fcol = $('fcol').value
		var ecol = $('ecol').value
		
		var query = `table=${tableindex}&access=${access}&fcol=${fcol}&ecol=${ecol}&strow=${strow}&cntrow=${cntrow}&is_tables=${is_tables}`
		get_content(query, 'POST', 'get_table.py', 'table')

		$('prevtxt').value = strow
		$('nexttxt').value = strow + cntrow
	}
}

function next()
{
	var tableindex = $('tableindex').value
	if (tableindex != -1)
	{
		var is_tables = $('is_tables').value
		var access = $('access').value
		var cntrow = parseInt($('cntrowhidden').value, 10)
		var strow = parseInt($('strow').value, 10)
		strow += cntrow
		$('strow').value = strow
		var fcol = $('fcol').value
		var ecol = $('ecol').value

		var query = `table=${tableindex}&access=${access}&fcol=${fcol}&ecol=${ecol}&strow=${strow}&cntrow=${cntrow}&is_tables=${is_tables}`
		get_content(query, 'POST', 'get_table.py', 'table')

		$('prevtxt').value = strow
		$('nexttxt').value = strow + cntrow
	}
}

function get_dependence(tableindex, rowid, is_tables) 
{
	var access = $('access').value
	var query = `tableindex=${tableindex}&rowid=${rowid}&is_tables=${is_tables}&access=${access}`
	get_content(query, 'POST', 'get_dependence.py', 'dependencies')
	$('dependencies').style.display = "inline"
}

function change_view(table_name)
{
	not_todisplay = $('cur_display').value
	$(`${not_todisplay}`).style.display = "none"
	$('cur_display').value = table_name
	$(table_name).style.display = "inline"
}

function insertdata(data)
{
	var ids = data.split(',')
	var query = "data="
	for (var i = 0; i < ids.length - 1; i++) 
	{
		query += `${$(ids[i]).value},`
	}
	query += `${$(ids[ids.length - 1]).value}&`
	query += `tableindex=${$('tableindex').value}`
	set_content(query, 'POST', 'set_insert.py')
}

function deletedata(data) 
{
	var ids = data.split(',')
	var query = "data="
	for (var i = 0; i < ids.length - 1; i++) 
	{
		query += `${$(ids[i]).value},`
	}
	query += `${$(ids[ids.length - 1]).value}&`
	query += `tableindex=${$('tableindex').value}`
	set_content(query, 'POST', 'set_delete.py')
}

function searchdata(data)
{
	var ids = data.split(',')
	var query = "data="
	for (var i = 0; i < ids.length - 1; i++) 
	{
		query += `${$(ids[i]).value},`
	}
	query += `${$(ids[ids.length - 1]).value}&`
	query += `tableindex=${$('tableindex').value}`
}