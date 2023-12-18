# from src.constants.api_constants import BASE_URL, APIConstants, base_url
import json
import os

import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_jsonschema(self):
        # URL, Headers, Payload,

        payload = payload_create_booking()
        print(payload)
        # payload.update({"firstname: "pramod","lastname:"dutta})
        payload["firstname"] = "Pramod"
        print(payload)

        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload, in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        response_json = response.json()

        file = os.getcwd() + "/schema.json"
        schema = self.load_schema(file)
        print(schema)
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.message)
