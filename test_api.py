import pytest
import requests_mock

from client import RandomDataAPI


@pytest.fixture
def users_data():
    return {
        "id": 5490,
        "uid": "7e734e55-328d-410f-a29a-b4203dfcd82a",
        "password": "FNHG4voOCB",
        "first_name": "Joe",
        "last_name": "Barrows",
        "username": "joe.barrows",
        "email": "joe.barrows@email.com",
        "avatar": "https://robohash.org/pariaturomnisquo.png?size=300x300&set=set1",
        "gender": "Non-binary",
        "phone_number": "+46 1-276-529-3104 x55499",
        "social_insurance_number": "262828478",
        "date_of_birth": "1987-12-18",
        "employment": {"title": "Education Consultant", "key_skill": "Confidence"},
        "address": {
            "city": "West Dominique",
            "street_name": "Jodee Tunnel",
            "street_address": "985 Bosco Street",
            "zip_code": "87786-9714",
            "state": "Connecticut",
            "country": "United States",
            "coordinates": {"lat": 76.31127593406052, "lng": -131.05593387019354},
        },
        "credit_card": {"cc_number": "5568-3558-7856-1043"},
        "subscription": {
            "plan": "Silver",
            "status": "Pending",
            "payment_method": "Money transfer",
            "term": "Monthly",
        },
    }


def test_get_users(users_data):
    api = RandomDataAPI()
    with requests_mock.Mocker() as m:
        m.get(f"https://random-data-api.com/api/v2/users?size=1", json=users_data)
        users = api.get_users()
        assert users == [users_data]


def test_get_average_date_of_birth():
    api = RandomDataAPI()
    with requests_mock.Mocker() as m:
        mock_users = [{"date_of_birth": "1990-10-10"}, {"date_of_birth": "1990-10-12"}]
        m.get(f"https://random-data-api.com/api/v2/users?size=2", json=mock_users)
        dob = api.get_average_date_of_birth(size=2)
        assert dob == "1990-10-11"
