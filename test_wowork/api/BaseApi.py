from test_wowork.utils.Utils import Utils


class BaseApi:
    def verbose(self,json_object):
        print(Utils.format(json_object))