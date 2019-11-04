from unittest import TestCase

import requests

from test_wowork.utils.Utils import Utils


class TestUtils(TestCase):
    def test_format(self):
        utils = Utils()
        print(utils.format(requests.get(url="https://testerhome.com/api/v3/topics.json?limit=2").json()))

