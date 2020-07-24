from typing import Dict

import pytest
from flask import json

from app import app


@pytest.fixture
def client():
    client = app.test_client()

    yield client


def exec_test(client, data: Dict, res: Dict):
    response = client.post('/', data=json.dumps(data), content_type='application/json')
    res_data = json.loads(response.data)
    assert res_data == res


def test_first_payment_date_monthly(client):
    exec_test(client, {
        "opened_date": "2020-07-23",
        "payments_frequency": 12
    }, {
        "first_payment_date": "2020-08-23"
    })


def test_first_payment_date_fortnightly(client):
    exec_test(client, {
        "opened_date": "2020-03-11",
        "payments_frequency": 24
    }, {
        "first_payment_date": "2020-03-15"
    })
