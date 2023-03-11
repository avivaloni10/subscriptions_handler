from unittest.mock import patch

from models.subscription import Subscription
from tests.integration_tests.subscription_endpoints.utils import *


@patch(UPDATE_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
@patch(GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
def test_update_subscription(get_subscription_by_name_mock, update_subscription_by_name_mock) -> None:
    get_subscription_by_name_mock.return_value = Subscription(**SUBSCRIPTION_DETAILS)
    update_subscription_by_name_mock.return_value = Subscription(**{**SUBSCRIPTION_DETAILS, **UPDATED_SUBSCRIPTION_DESCRIPTION})

    response = client.put(url=f"/subscriptions/{SUBSCRIPTION_DETAILS['name']}", json={"parameter": UPDATED_SUBSCRIPTION_DESCRIPTION})
    assert response.status_code == 200
    assert response.json() == {'code': 200,
                               'message': 'Subscription updated successfully',
                               'result': {**SUBSCRIPTION_DETAILS, **UPDATED_SUBSCRIPTION_DESCRIPTION},
                               'status': 'OK'}


@patch(GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
def test_update_subscription_subscription_not_exists(get_subscription_by_name_mock) -> None:
    get_subscription_by_name_mock.return_value = None

    response = client.put(url=f"/subscriptions/{SUBSCRIPTION_DETAILS['name']}", json={"parameter": UPDATED_SUBSCRIPTION_DESCRIPTION})
    assert response.status_code == 404
    assert response.json() == {"detail": "Subscription not found"}


@patch(UPDATE_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
@patch(GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH)
def test_update_subscription_not_update_name_password_phone_number(get_subscription_by_name_mock, update_subscription_by_name_mock) -> None:
    get_subscription_by_name_mock.return_value = Subscription(**SUBSCRIPTION_DETAILS)
    update_subscription_by_name_mock.return_value = Subscription(**SUBSCRIPTION_DETAILS)

    response = client.put(url=f"/subscriptions/{SUBSCRIPTION_DETAILS['name']}",
                          json={"parameter": UPDATED_SUBSCRIPTION_NAME})
    assert response.status_code == 200
    assert response.json() == {'code': 200,
                               'message': 'Subscription updated successfully',
                               'result': SUBSCRIPTION_DETAILS,
                               'status': 'OK'}
