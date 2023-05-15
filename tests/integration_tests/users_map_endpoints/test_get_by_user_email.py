from unittest.mock import patch

from models.user_subscription_map import UserSubscriptionMap
from tests.integration_tests.users_map_endpoints.utils import *


@patch(GET_SUBSCRIPTIONS_BY_USER_EMAIL_IMPORT_PATH)
def test_get_by_user_email(get_subscriptions_by_user_email_mock) -> None:
    get_subscriptions_by_user_email_mock.return_value = UserSubscriptionMap(**USER_SUBSCRIPTION_MAP_DETAILS)

    response = client.get(url=f"/users_map/{USER_SUBSCRIPTION_MAP_DETAILS['user_email']}")
    assert response.status_code == 200
    assert response.json() == {
        'code': 200,
        'message': 'UserSubscriptionMap fetched successfully',
        'result': USER_SUBSCRIPTION_MAP_DETAILS,
        'status': 'OK'
    }


@patch(GET_SUBSCRIPTIONS_BY_USER_EMAIL_IMPORT_PATH)
def test_get_by_user_email_user_email_not_exists(get_subscriptions_by_user_email_mock) -> None:
    get_subscriptions_by_user_email_mock.return_value = None

    response = client.get(url="/users_map/metoonaf@gmail.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "No subscriptions for this user."}
