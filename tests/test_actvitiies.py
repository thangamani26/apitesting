import pytest
from utils.apis import APIS


def test_get_all_activities():
    apis = APIS()

    response = apis.get_all_activities()
    print(response.status_code)
    print(response.json())
    print(response.headers)

    assert response.status_code == 200
