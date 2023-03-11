import datetime
from typing import Dict, Optional

from sqlalchemy.exc import IntegrityError
from starlette.testclient import TestClient
from main import app

client = TestClient(app)

CREATE_USER_SUBSCRIPTION_MAP_IMPORT_PATH = "dal.user_subscription_map.create_user_subscription_map"
GET_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH = "dal.user_subscription_map.get_user_subscription_map_by_user_email_subscription_name"
GET_USER_SUBSCRIPTION_MAPS_IMPORT_PATH = "dal.user_subscription_map.get_user_subscription_maps"
UPDATE_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH = "dal.user_subscription_map.update_user_subscription_map_by_user_email_subscription_name"
DELETE_USER_SUBSCRIPTION_MAP_BY_USER_EMAIL_SUBSCRIPTION_NAME_IMPORT_PATH = "dal.user_subscription_map.delete_user_subscription_map_by_user_email_subscription_name"

USER_SUBSCRIPTION_MAP_DETAILS = {
    'subscription_name': 'a',
    'user_email': 'a@gmail.com',
    'card_owner_id': '342543948',
    'card_number': '1111222233334444',
    'cvv': '111',
    'start_date': datetime.datetime.now().timestamp(),
    'expiration_date': (datetime.datetime.now() + datetime.timedelta(6 * 30)).timestamp()
}

UPDATED_USER_SUBSCRIPTION_MAP_CARD_DETAILS = {
    'card_owner_id': '342543948',
    'card_number': '1111222233334444',
    'cvv': '111'
}

UPDATED_USER_SUBSCRIPTION_MAP_IMMUTABLES = {
    'subscription_name': 'a',
    'user_email': 'a@gmail.com',
    'start_date': datetime.datetime.now().timestamp(),
    'expiration_date': (datetime.datetime.now() + datetime.timedelta(6 * 30)).timestamp()
}


def validate_user_subscription_map_creation(user_subscription_map_details: Dict, expected_status_code: int = 200,
                                            expected_result: Optional[Dict] = None):
    if expected_result is None:
        expected_result = {'code': 200, 'message': 'UserSubscriptionMap created successfully', 'status': 'OK'}
    response = client.post(url="/user_subscription_maps", json={"parameter": user_subscription_map_details})
    assert response.status_code == expected_status_code
    assert response.json() == expected_result


def validate_user_subscription_map_deletion(user_subscription_map_details: Dict, expected_status_code: int = 200,
                                            expected_result: Optional[Dict] = None):
    if expected_result is None:
        expected_result = {'code': 200, 'message': 'UserSubscriptionMap deleted successfully', 'status': 'OK'}
    response = client.delete(url=f"/user_subscription_maps/{user_subscription_map_details['user_email']}/{user_subscription_map_details['subscription_name']}")
    assert response.status_code == expected_status_code
    assert response.json() == expected_result
