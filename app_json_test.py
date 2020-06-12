import app_json

def test_index_post():
    app = Flask(__name__)
    client = app_json.test_client()
    url = '/'
    response= client.get(url)

    assert response.get_data() == { "name": " Monica",
    "school": " University of Wisconsin",
    "sports": " rowing" }
    assert response.status_code == 200

def test_index_get():
	app = Flask(__name__)
	client = app_json.test_client()
	url = '/get'
	response= client.get(url) 

	assert response.get_data() == {"key":[0,1,2,3]}
	assert response.status_code == 200
