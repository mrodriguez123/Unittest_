import requests
import pytest

# https://github.com/basdijkstra/ota-examples/tree/master/python-requests
# https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/

# website returns information regarding the place 
# example: http://api.zippopotam.us/us/33129 returns a json with:
# {"post code": "33129", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Miami", "longitude": "-80.2013", "state": "Florida", "state abbreviation": "FL", "latitude": "25.7559"}]}

# example: http://api.zippopotam.us/es/28008
# {"post code": "28008", "country": "Spain", "country abbreviation": "ES", "places": [{"place name": "Madrid", "longitude": "-3.7158", "state": "Madrid", "state abbreviation": "M", "latitude": "40.4256"}]}

# can print response as a json
response = requests.get("http://api.zippopotam.us/ca/B2A")
response_body = response.json()
print(response_body)

response = requests.get("http://api.zippopotam.us/es/28008")
response_body = response.json()
print(response_body)

# find num of post codes in miami
response = requests.get("http://api.zippopotam.us/us/fl/miami")
response_body = response.json()
places = response_body['places']
zips = []
for i in range(len(places)):
    if places[i]["post code"] not in zips:
        zips.append(places[i]["post code"])

print(len(zips))

# rest api testing 
# can either run in command line to see if tests pass 
# or run in sublime, add a print "test passed message"

#checks status code 
def test_get_locations_33129_status_code_200():
     response = requests.get("http://api.zippopotam.us/us/33129")
     assert response.status_code == 200

# checks content type 
def test_get_locations_33129_content_type_json():
    response = requests.get("http://api.zippopotam.us/us/33129")
    assert response.headers['Content-Type'] == "application/json"

# checks the country is correct
def test_get_locations_33129_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/us/33129")
    response_body = response.json()
    assert response_body["country"] == "United States"

# checks the city is correct 
def test_get_locations_33129_city_equals_miami():
    response = requests.get("http://api.zippopotam.us/us/33129")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Miami"

# checks the lenght of the place returned is one (only one place)
# places contains a list with one dictionary
def test_get_locations_33129_one_place_is_returned():
    response = requests.get("http://api.zippopotam.us/us/33129")
    response_body = response.json()
    assert len(response_body["places"]) == 1

def test_get_number_zip_codes():
    response = requests.get("https://api.zippopotam.us/us/fl/miami")
    response_body = response.json()
    assert len(response_body["places"]) == 105


