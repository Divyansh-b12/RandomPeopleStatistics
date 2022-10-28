"""
The goal of this test is to create an python API client for the following user api: https://random-data-api.com/api/v2/users

Create an API client to call the api 10 times.
Use your client to return statistics on the users. Give the average age of the 10 users (use the date_of_birth property to determine age).
Return the top 5 oldest users and the top 5 youngest users.
(Bonus) Add an option to your client to use a caching system instead of calling the API directly.
(Bonus) Add unit tests to your client.
Please use the typing module for variables, function and method definitions.
"""
import datetime
import logging
import time
from functools import lru_cache
from typing import List

import requests

logger = logging.getLogger(__name__)


class RandomDataAPI:
    def __init__(self):
        self.domain = "random-data-api.com"
        self.scheme = "https"

    @lru_cache
    def get_users(self, size: int = 1) -> List[dict]:
        url = f"{self.scheme}://{self.domain}/api/v2/users?size={size}"
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as exc:
            logger.error("unable to get users")
            return []
        return response.json()

    def get_average_date_of_birth(self, size: int = 10) -> str:
        # Calculate average date of birth for the users
        users = self.get_users(size=size)
        dobs = []
        for user in users:
            dob = datetime.datetime.strptime(user["date_of_birth"], "%Y-%m-%d")
            timestamp = time.mktime(dob.timetuple())
            dobs.append(timestamp)
        average = sum(dobs) / len(dobs)
        average_dob = datetime.datetime.fromtimestamp(average)
        return average_dob.strftime("%Y-%m-%d")
