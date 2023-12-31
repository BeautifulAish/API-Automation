# HTTP Status verification

def verify_http_status_code(response_data, expected_data):
    print(response_data.status_code)
    print(expected_data)
    assert_response_data.status_code == expected_data, "Expected HTTP status code" + str(expect_Data)

def verify_json_key_for_not_null(key):
    assert key != 0, "Key is non Empty" + key
    assert key > 0, "Key is greater than zero"

def verify_response(key):
    assert key is not None  #verify token is not empty

def verify_response():
    pass


# Common Verification
# HTTP Status code
# Headers
# Data Verification
# JSON Schema

