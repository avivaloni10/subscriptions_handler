from unittest.mock import patch

import pytest

from copy import deepcopy

from sqlalchemy.exc import IntegrityError

from models.user_subscription_map import UserSubscriptionMap
from tests.integration_tests.user_subscription_map_endpoints.utils import *


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map(create_user_subscription_map_mock) -> None:
    create_user_subscription_map_mock.return_value = UserSubscriptionMap(**USER_SUBSCRIPTION_MAP_DETAILS)

    validate_user_subscription_map_creation(user_subscription_map_details=USER_SUBSCRIPTION_MAP_DETAILS)


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map_no_user_email(create_user_subscription_map_mock) -> None:
    create_user_subscription_map_mock.side_effect = IntegrityError(None, None, None)

    user_subscription_map_details = deepcopy(USER_SUBSCRIPTION_MAP_DETAILS)
    del user_subscription_map_details["user_email"]
    with pytest.raises(IntegrityError):
        validate_user_subscription_map_creation(user_subscription_map_details=user_subscription_map_details)


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map_no_subscription_name(create_user_subscription_map_mock) -> None:
    create_user_subscription_map_mock.side_effect = IntegrityError(None, None, None)

    user_subscription_map_details = deepcopy(USER_SUBSCRIPTION_MAP_DETAILS)
    del user_subscription_map_details["subscription_name"]
    with pytest.raises(IntegrityError):
        validate_user_subscription_map_creation(user_subscription_map_details=user_subscription_map_details)


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map_card_owner_id(create_user_subscription_map_mock) -> None:
    create_user_subscription_map_mock.side_effect = IntegrityError(None, None, None)

    user_subscription_map_details = deepcopy(USER_SUBSCRIPTION_MAP_DETAILS)
    del user_subscription_map_details["card_owner_id"]
    with pytest.raises(IntegrityError):
        validate_user_subscription_map_creation(user_subscription_map_details=user_subscription_map_details)


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map_no_card_number(create_user_subscription_map_mock) -> None:
    create_user_subscription_map_mock.side_effect = IntegrityError(None, None, None)

    user_subscription_map_details = deepcopy(USER_SUBSCRIPTION_MAP_DETAILS)
    del user_subscription_map_details["card_number"]
    with pytest.raises(IntegrityError):
        validate_user_subscription_map_creation(user_subscription_map_details=user_subscription_map_details)


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map_no_cvv(create_user_subscription_map_mock) -> None:
    create_user_subscription_map_mock.side_effect = IntegrityError(None, None, None)

    user_subscription_map_details = deepcopy(USER_SUBSCRIPTION_MAP_DETAILS)
    del user_subscription_map_details["cvv"]
    with pytest.raises(IntegrityError):
        validate_user_subscription_map_creation(user_subscription_map_details=user_subscription_map_details)


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map_start_date_no_expiration_date(create_user_subscription_map_mock) -> None:
    user_subscription_map_details = deepcopy(USER_SUBSCRIPTION_MAP_DETAILS)
    del user_subscription_map_details["start_date"]
    del user_subscription_map_details["expiration_date"]

    create_user_subscription_map_mock.return_value = UserSubscriptionMap(**user_subscription_map_details)

    validate_user_subscription_map_creation(user_subscription_map_details=user_subscription_map_details)


@patch(CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH)
def test_create_user_subscription_map_user_subscription_map_already_exists(create_user_subscription_map_mock) -> None:
    create_user_subscription_map_mock.side_effect = [UserSubscriptionMap(**USER_SUBSCRIPTION_MAP_DETAILS), IntegrityError(None, None, None)]

    validate_user_subscription_map_creation(user_subscription_map_details=USER_SUBSCRIPTION_MAP_DETAILS)
    with pytest.raises(IntegrityError):
        validate_user_subscription_map_creation(user_subscription_map_details=USER_SUBSCRIPTION_MAP_DETAILS)
