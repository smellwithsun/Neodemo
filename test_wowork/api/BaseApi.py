from test_wowork.utils.Utils import Utils


class BaseApi:
    json_data = None
    @classmethod
    def verbose(cls,json_object):
        print(Utils.format(json_object))
    @classmethod
    def jaonpath(cls,expr):
       return Utils.jsonpath(cls.json_data,expr)