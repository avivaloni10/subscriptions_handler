from typing import Dict, Optional

from starlette.testclient import TestClient
from main import app

client = TestClient(app)

CREATE_SUBSCRIPTION_IMPORT_PATH = "dal.subscription.create_subscription"
GET_SUBSCRIPTION_BY_NAME_IMPORT_PATH = "dal.subscription.get_subscription_by_name"
GET_SUBSCRIPTIONS_IMPORT_PATH = "dal.subscription.get_subscriptions"
UPDATE_SUBSCRIPTION_BY_NAME_IMPORT_PATH = "dal.subscription.update_subscription_by_name"
DELETE_SUBSCRIPTION_BY_NAME_IMPORT_PATH = "dal.subscription.delete_subscription_by_name"

SUBSCRIPTION_DETAILS = {'name': 'a', 'description': 'aaa'}

UPDATED_SUBSCRIPTION_DESCRIPTION = {'description': 'bbb'}

UPDATED_SUBSCRIPTION_NAME = {'name': 'b'}


def validate_subscription_creation(subscription_details: Dict, expected_status_code: int = 200, expected_result: Optional[Dict] = None):
    if expected_result is None:
        expected_result = {'code': 200, 'message': 'Subscription created successfully', 'status': 'OK'}
    response = client.post(url="/subscriptions", json={"parameter": subscription_details})
    assert response.status_code == expected_status_code
    assert response.json() == expected_result


def validate_subscription_deletion(subscription_details: Dict, expected_status_code: int = 200, expected_result: Optional[Dict] = None):
    if expected_result is None:
        expected_result = {'code': 200, 'message': 'Subscription deleted successfully', 'status': 'OK'}
    response = client.delete(url=f"/subscriptions/{subscription_details['name']}")
    assert response.status_code == expected_status_code
    assert response.json() == expected_result
