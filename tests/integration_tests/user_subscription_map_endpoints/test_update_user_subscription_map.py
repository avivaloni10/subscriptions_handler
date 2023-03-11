from unittest.mock import patch

from models.user_subscription_map import UserSubscriptionMap
from tests.integration_tests.user_subscription_map_endpoints.utils import *


@patch(UPDATE_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH)
@patch(GET_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH)
def test_update_user_subscription_map(get_user_subscription_map_by_user_email_subscription_name_mock, update_user_subscription_map_by_user_email_subscription_name_mock) -> None:
    get_user_subscription_map_by_user_email_subscription_name_mock.return_value = UserSubscriptionMap(**USER_SUBSCRIPTION_MAP_DETAILS)
    update_user_subscription_map_by_user_email_subscription_name_mock.return_value = UserSubscriptionMap(**{**USER_SUBSCRIPTION_MAP_DETAILS, **UPDATED_USER_SUBSCRIPTION_MAP_CARD_DETAILS})

    response = client.put(url=f"/user_subscription_maps/{USER_SUBSCRIPTION_MAP_DETAILS['user_email']}/{USER_SUBSCRIPTION_MAP_DETAILS['subscription_name']}", json={"parameter": UPDATED_USER_SUBSCRIPTION_MAP_CARD_DETAILS})
    assert response.status_code == 200
    assert response.json() == {'code': 200,
                               'message': 'UserSubscriptionMap updated successfully',
                               'result': {**USER_SUBSCRIPTION_MAP_DETAILS, **UPDATED_USER_SUBSCRIPTION_MAP_CARD_DETAILS},
                               'status': 'OK'}


@patch(GET_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH)
def test_update_user_subscription_map_user_subscription_map_not_exists(get_user_subscription_map_by_user_email_subscription_name_mock) -> None:
    get_user_subscription_map_by_user_email_subscription_name_mock.return_value = None

    response = client.put(url=f"/user_subscription_maps/metoonaf@gmail.com/blablabla", json={"parameter": UPDATED_USER_SUBSCRIPTION_MAP_CARD_DETAILS})
    assert response.status_code == 404
    assert response.json() == {"detail": "UserSubscriptionMap not found"}


@patch(UPDATE_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH)
@patch(GET_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH)
def test_update_user_subscription_map_not_update_immutables(get_user_subscription_map_by_user_email_subscription_name_mock, update_user_subscription_map_by_user_email_subscription_name_mock) -> None:
    get_user_subscription_map_by_user_email_subscription_name_mock.return_value = UserSubscriptionMap(**USER_SUBSCRIPTION_MAP_DETAILS)
    update_user_subscription_map_by_user_email_subscription_name_mock.return_value = UserSubscriptionMap(**USER_SUBSCRIPTION_MAP_DETAILS)

    response = client.put(url=f"/user_subscription_maps/{USER_SUBSCRIPTION_MAP_DETAILS['user_email']}/{USER_SUBSCRIPTION_MAP_DETAILS['subscription_name']}",
                          json={"parameter": UPDATED_USER_SUBSCRIPTION_MAP_IMMUTABLES})
    assert response.status_code == 200
    assert response.json() == {'code': 200,
                               'message': 'UserSubscriptionMap updated successfully',
                               'result': USER_SUBSCRIPTION_MAP_DETAILS,
                               'status': 'OK'}
