import requests # http requests
import json
BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list(id = '7'):
	data = json.dumps({})
	if id is not None:
		data = json.dumps({
			"id": id,
		})
	r = requests.get(BASE_URL+ENDPOINT, data =data)
	print(r.status_code)
	status_code = r.status_code
	if r.status_code != 200:
		print('not a good sign!')
	data = r.json()
	return data

print(get_list())

def create_update():
	new_data = {
		'user': 1,	
		'content': "another new content"
	}
	r = requests.post(BASE_URL+ENDPOINT, data = json.dumps(new_data))
	print(r.headers)
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		return r.json()
	return r.text

#print(create_update())

def do_obj_update():
	new_data = {	
		"id": 3,
		"content": "another new content updated"
	}
	r = requests.put(BASE_URL+ENDPOINT, data = json.dumps(new_data)) 
	print(r.json())
	print(r.headers)
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		return r.json()
	return r.text

def do_obj_delete():
	new_data = {	
		"id": 3,
		"content": "new obj data"
	}
	r = requests.delete(BASE_URL+ENDPOINT, data = json.dumps(new_data))
	print(r.json())
	print(r.headers)
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		return r.json()
	return r.text

#print(do_obj_update())