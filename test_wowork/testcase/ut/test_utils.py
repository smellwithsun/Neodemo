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
    def test_merge(self):
        utils = Utils()
        dict1 ={"a":3,"b":4}
        dict2={"c":5}
        print(utils.Merge(dict1,dict2))

