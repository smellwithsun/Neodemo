import requests

from test_wowork.api.BaseApi import BaseApi


class WeWork(BaseApi):
    corpid = "wwe96617ef560b27ec"
    concat_secret = 'qS_a73QUySfC_XLoP__0sm-Q3wyraczCWTgVaoSeKcQ'
    agent_id = 1000002
    agent_secret = "8pHe2Qdy9OqqBdgkIa4Z3RyHCi-wzPc0jZyyOJ8nvk0"
    acces_token = None
    @classmethod
    def get_token(cls):
        if cls.acces_token is None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r=requests.get(url,params={"corpid":cls.corpid,
            "corpsecret":cls.concat_secret}).json()
            cls.verbose(r)
            cls.acces_token=r["access_token"]
        return cls.acces_token


