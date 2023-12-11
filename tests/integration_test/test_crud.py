import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests,put_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):

    def test_create_token(self):
        response = post_requests(
            url=APIConstants.url_create_token(),
            headers=common_headers_json(),
            auth = None,
            payload= payload_create_token(), in_json=False
        )
        verify_http_status_code(response,200)
        token = response.json()["token"]
        print(token)
        verify_response_key_should_not_be_none(token)
        return token


    def test_create_booking(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        return bookingid
    def test_update_booking(self): # Token and Booking ID from the Create Booking, Token
        token = "58d8c38d7019749"
        put_url = APIConstants.url_create_booking() + "/3483"
        auth = ("admin","password123")

        response = put_requests(url=put_url, auth=auth, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response.json())

    def test_delete_booking(self):
        pass
