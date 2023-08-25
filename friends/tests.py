from rest_framework.test import APIClient, APITestCase

# Create your tests here.


class TestFriends(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.friend_request = {
            "total_price": 23000,
            "user": [
                [1, 2],
                [3, 4],
                [5, 6]
            ]
        }

        