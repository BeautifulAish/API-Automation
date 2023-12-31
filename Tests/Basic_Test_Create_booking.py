import requests
def test_sample1():
    assert 5 == 5

def test_sample2():
    assrt4 == 4

def test_sample3():
    assert 6 == 6

def test_getrequest():

id = "1978"
url = "https://restful-booker.herokuapp.com/booking/"
full_Url = url + id
print(full_url)
response_body = requests.get(full_url)
assert response_body.status_code == 200
# if status code != 200 it will give error else it will not give error

# Conversion data - json
data = response_body.json
print(type(data))

# assertions

# Verification of keys
assert 'firstname' in data, "FirstName key is present"  # We are using in fun - definitely it is dict data type
assert 'lastName' in data, "LastName key is present"

# Verification of data
assert data["firstName"] == "Josh", "Incorrect firstName is Josh"
assert data["lastName"] == "Allen", "Incorrect lastName"
assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Message"


