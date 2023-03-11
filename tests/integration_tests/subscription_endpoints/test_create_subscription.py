from unittest.mock import patch

import pytest

from copy import deepcopy

from sqlalchemy.exc import IntegrityError

from models.subscription import Subscription
from tests.integration_tests.subscription_endpoints.utils import *


@patch(CREATE_SUBSCRIPTION_IMPORT_PATH)
def test_create_subscription(create_subscription_mock) -> None:
    create_subscription_mock.return_value = Subscription(**SUBSCRIPTION_DETAILS)

    validate_subscription_creation(subscription_details=SUBSCRIPTION_DETAILS)


@patch(CREATE_SUBSCRIPTION_IMPORT_PATH)
def test_create_subscription_no_name(create_subscription_mock) -> None:
    create_subscription_mock.side_effect = IntegrityError(None, None, None)

    subscription_details = deepcopy(SUBSCRIPTION_DETAILS)
    del subscription_details["name"]
    with pytest.raises(IntegrityError):
        validate_subscription_creation(subscription_details=subscription_details)


@patch(CREATE_SUBSCRIPTION_IMPORT_PATH)
def test_create_subscription_no_description(create_subscription_mock) -> None:
    create_subscription_mock.side_effect = IntegrityError(None, None, None)

    subscription_details = deepcopy(SUBSCRIPTION_DETAILS)
    del subscription_details["description"]
    with pytest.raises(IntegrityError):
        validate_subscription_creation(subscription_details=subscription_details)


@patch(CREATE_SUBSCRIPTION_IMPORT_PATH)
def test_create_subscription_subscription_already_exists(create_subscription_mock) -> None:
    create_subscription_mock.side_effect = [Subscription(**SUBSCRIPTION_DETAILS), IntegrityError(None, None, None)]

    validate_subscription_creation(subscription_details=SUBSCRIPTION_DETAILS)
    with pytest.raises(IntegrityError):
        validate_subscription_creation(subscription_details=SUBSCRIPTION_DETAILS)
