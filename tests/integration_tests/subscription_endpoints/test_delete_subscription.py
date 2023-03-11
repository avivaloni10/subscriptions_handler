from unittest.mock import patch

from models.subscription import Subscription
from tests.integration_tests.subscription_endpoints.utils import *


@patch(DELETE_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
@patch(GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
def test_delete_subscription(get_subscription_by_name_mock, delete_subscription_by_name_mock) -> None:
    get_subscription_by_name_mock.return_value = Subscription(**SUBSCRIPTION_DETAILS)
    delete_subscription_by_name_mock.return_value = None

    validate_subscription_deletion(SUBSCRIPTION_DETAILS)


@patch(GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
def test_delete_subscription_subscription_not_exists(get_subscription_by_name_mock) -> None:
    get_subscription_by_name_mock.return_value = None

    validate_subscription_deletion(SUBSCRIPTION_DETAILS, expected_status_code=404, expected_result={"detail": "Subscription not found"})
