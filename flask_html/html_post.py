import requests 

information= {'name': 'Moni', 'school': 'University of Wisconsin'}
r = requests.post('https://httpbin.org/post', data= information)
r_dict = r.json()
form = r_dict['form']

def post_text():
	return form



