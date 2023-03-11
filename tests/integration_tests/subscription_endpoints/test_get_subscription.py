from unittest.mock import patch

from models.subscription import Subscription
from tests.integration_tests.subscription_endpoints.utils import *


@patch(GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
def test_get_subscription(get_subscription_by_name_mock) -> None:
    get_subscription_by_name_mock.return_value = Subscription(**SUBSCRIPTION_DETAILS)

    response = client.get(url=f"/subscriptions/{SUBSCRIPTION_DETAILS['name']}")
    assert response.status_code == 200
    assert response.json() == {
        'code': 200,
        'message': 'Subscription fetched successfully',
        'result': SUBSCRIPTION_DETAILS,
        'status': 'OK'
    }


@patch(GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
def test_get_subscription_name_not_exists(get_subscription_by_name_mock) -> None:
    get_subscription_by_name_mock.return_value = None

    response = client.get(url="/subscriptions/metoonaf@gmail.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "Subscription not found"}
