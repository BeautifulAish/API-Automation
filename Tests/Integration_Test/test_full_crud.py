from Src.helpers.api_constants_wrapper import post_requests
#from Src.Constants.API_constants import BASE_URL, APIConstants, base_url
from Src.helpers.api_constants_wrapper import APIConstants
from Src.helpers.utils import common_headers_json
from Src.helpers.payload_manager import payload_create_booking
from Src.helpers.common_verification import verify_response, verify_http_status_code

import pytest

Class Testcreatebooking(object):
@pytest.mark.positive

def test_create_token(self):
 response = post_requests(
  url=APIConstants.url_create_token()
  auth = None
 )

def test_create_booking(self):
 pass

def test_update_booking(self): #Token and Booking from Create Booking, Token
 pass

def test_delete_booking(self):
 pass
