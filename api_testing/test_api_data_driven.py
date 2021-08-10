import requests
import pytest

#finish this 
#make more examples

#two files with this and part 1
#refresh github uploading 

# https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-2-data-driven-tests/
# https://assertible.com/blog/7-http-methods-every-web-developer-should-know-and-how-to-test-them


miami = ("us", "33129", "Miami")
madison = ("us", "53715", "Madison")
madrid = ("es", "28008", "Madrid")

test_zip_codes1 = (miami, madison, madrid)

# data driven tests are supported using the marker @pytest.mark.parametrize, takes two parameters: 
# first one tells pytest how to map the data (tuple) which is the second argument 
# so one for each element in the tuple
# it automatically runs it for every item in the test_zip_codes tuple (in command line run pytest file_name.py)

@pytest.mark.parametrize("country_code, zip_code, expected_name", test_zip_codes1)
def test_place_name_from_zip_code1(country_code, zip_code, expected_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_name

france = ("FR", "75001", "Paris 01 Louvre")
santo_domingo = ("DO", "10122", "Centro Olimpico ")
sydney = ("AU", "2006", "The University Of Sydney")
test_zip_codes2 = (france, santo_domingo, sydney)

@pytest.mark.parametrize("country_code, zip_code, expected_name", test_zip_codes2)
def test_place_name_from_zip_code2(country_code, zip_code, expected_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_name


# website with json data to use for practice
# https://jsonplaceholder.typicode.com/

# example of user id 1:
res = requests.get("https://jsonplaceholder.typicode.com/todos/1")
res_body = res.json()
print("response for 'https://jsonplaceholder.typicode.com/todos/1': ")
print(res_body)

def test_status_code_equals_200():
     response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
     assert response.status_code == 200
     print("status code ok")

# call it to check in sublime, if not can run through terminal
test_status_code_equals_200()

# "https://jsonplaceholder.typicode.com/todos/1"
# "https://jsonplaceholder.typicode.com/users/6/posts"
# "https://jsonplaceholder.typicode.com/users/6"
# "https://jsonplaceholder.typicode.com/posts/78"


def test_user_6_name():
    response = requests.get("https://jsonplaceholder.typicode.com/users/6")
    response_body = response.json()
    assert response_body["name"] == "Mrs. Dennis Schulist"
    print("user name matches")

test_user_6_name()

def test_user_6_geo():
    response = requests.get("https://jsonplaceholder.typicode.com/users/6")
    response_body = response.json()
    assert response_body["address"]["geo"]['lat'] == '-71.4197'
    assert response_body["address"]["geo"]['lng'] == '71.7478'
    print("geo data matches")

test_user_6_geo()

def test_post_78_title():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/78")
    response_body = response.json()
    assert response_body["title"] == "quam voluptatibus rerum veritatis"
    print("post 78 title matches")

test_post_78_title()

def test_number_of_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response_body = response.json()
    assert len(response_body) == 10
    print("number of users matches")

test_number_of_users()

response = requests.get("https://jsonplaceholder.typicode.com/users/10")
response_body = response.json()
print(response_body['name'] == "Clementina DuBuque")

dennis = ("users", "6", "Mrs. Dennis Schulist")
nicholas = ("users", "8", "Nicholas Runolfsdottir V")
clementina = ("users", "10", "Clementina DuBuque")
users = (dennis, nicholas, clementina)

@pytest.mark.parametrize("type, id, expected_name", users)
def test_name_from_id(type, id, expected_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{type}/{id}")
    response_body = response.json()
    assert response_body['name'] == expected_name

# code on updating / posting from https://jsonplaceholder.typicode.com/guide



