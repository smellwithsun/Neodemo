from unittest import TestCase

import requests

from test_wowork.utils.Utils import Utils


class TestUtils(TestCase):
    def test_format(self):
        utils = Utils()
        print(utils.format(requests.get(url="https://testerhome.com/api/v3/topics.json?limit=2").json()))

    def test_jsonpath(self):
        r = requests.get(url="https://testerhome.com/api/v3/topics.json?limit=2").json()
        assert (Utils.jsonpath(r, "$.topics[?(@.excellent==0)]")[0]["id"])>20000

