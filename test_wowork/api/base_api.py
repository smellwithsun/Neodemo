import requests
from test_wowork.utils.Utils import Utils


class BaseApi:
    proxies = {
        'http': 'http://127.0.0.1:8898',
        'https': 'http://127.0.0.1:8898',
    }
    json_data = None
    @classmethod
    def verbose(cls,json_object=json_data):
        print(Utils.format(json_object))
    @classmethod
    def jaonpath(cls,expr):
       return Utils.jsonpath(cls.json_data,expr)

    @classmethod
    def send_data(cls, method, url, acces_token,param:dict):
        cls.json_data = requests.request(method,url,
                                         params=Utils.Merge({"access_token":acces_token},param),
                                         proxies=cls.proxies,verify=False).json()
        cls.verbose(cls.json_data)
        return cls.json_data


