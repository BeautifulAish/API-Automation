# Assertion - Using Assert
# Using Pytest library
import requests


def main():


id = "111"
Url = "https://restful-booker.herokuapp.com/booking/"
full_Url = Url + id
print(full_url)
response_body = requests.get(full_url)
assert response_body.status_code == 200

# if status code != 200 it will give error else it will not give error
# Conversion data - json

data = response_body.json()
print(type(data))

# assertions
# Verification of keys  #Assume data is a dictionary
assert 'firstname' in data, "Incorrect firstname"
assert 'lastname' in data, "lastname key is present"

print(data)

# Verification of data
assert data["firstname"] == "Jim", "Incorrect firstname is Jim"
assert data["lastname"] == "Brown", "Incorrect lastname"
assert_data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Message "

if __name__ == '__main__':
    main()
