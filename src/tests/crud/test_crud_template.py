# Conftest

# Create Token
# Create BookingId
# Update the Booking(Put) - BookingID, Token
# Delete the Booking

# Verify that created booking id when we update we are able to update it and delete it also

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.API_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utility import *


class TestCRUDBooking(object):
    def test_update_booking_id_token(self):
        pass

    def test_delete_booking_id(self):
        pass
