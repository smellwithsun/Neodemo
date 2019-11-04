import json

import jsonpath as jsonpath


class Utils:
    @classmethod
    def format(cls,json_object):
      return json.dumps(json_object,indent=2)
    @classmethod
    def jsonpath(cls,json_object,expr):
       return jsonpath.jsonpath(json_object,expr)