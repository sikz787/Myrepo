import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests, put_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch


class TestCreateBooking(object):



    def test_update_booking(self, create_token,
                            create_booking):  # Token/ Basic Auth and Booking ID from the Create Booking, Token
        bookindId = create_booking
        put_url = APIConstants.url_create_booking() + "/" + str(bookindId)

        response = put_requests(url=put_url, headers=common_headers_for_put_delete_patch(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        print(response.json())

    def test_delete_booking(self, create_token, create_booking):  # Token and Booking ID from the Create Booking, Token
        bookindId = create_booking
        delete_url = APIConstants.url_create_booking() + "/" + str(bookindId)

        response = put_requests(url=delete_url, headers=common_headers_for_put_delete_patch(), auth=None,
                                payload=None, in_json=False)
        print(response.json())
