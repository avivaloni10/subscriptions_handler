from unittest.mock import patch

from models.user_subscription_map import UserSubscriptionMap
from tests.integration_tests.user_subscription_map_endpoints.utils import *


@patch(GET_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH)
def test_get_user_subscription_map(get_user_subscription_map_by_user_email_subscription_name_mock) -> None:
    get_user_subscription_map_by_user_email_subscription_name_mock.return_value = UserSubscriptionMap(**USER_SUBSCRIPTION_MAP_DETAILS)

    response = client.get(url=f"/user_subscription_maps/{USER_SUBSCRIPTION_MAP_DETAILS['user_email']}/{USER_SUBSCRIPTION_MAP_DETAILS['subscription_name']}")
    assert response.status_code == 200
    assert response.json() == {
        'code': 200,
        'message': 'UserSubscriptionMap fetched successfully',
        'result': USER_SUBSCRIPTION_MAP_DETAILS,
        'status': 'OK'
    }


@patch(GET_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH)
def test_get_user_subscription_map_user_email_subscription_name_not_exists(get_user_subscription_map_by_user_email_subscription_name_mock) -> None:
    get_user_subscription_map_by_user_email_subscription_name_mock.return_value = None

    response = client.get(url="/user_subscription_maps/metoonaf@gmail.com/blablabla")
    assert response.status_code == 404
    assert response.json() == {"detail": "UserSubscriptionMap not found"}
