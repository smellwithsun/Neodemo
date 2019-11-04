from test_wowork.api.BaseApi import BaseApi
from test_wowork.api.wework import WeWork
import requests

from test_wowork.api.wework import WeWork
from test_wowork.utils.Utils import Utils


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    creat_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    proxies = {
        'http': 'http://127.0.0.1:8898',
        'https': 'http://127.0.0.1:8898',
    }
    headers ={'content-type': 'application/json; charset=utf-8', }
    update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

    def list(self,id):
        self.json_data= requests.get(self.list_url,params={"access_token":WeWork.get_token(),"id":id}).json()
        self.verbose(self.json_data)
        return self.json_data
    def creat(self,name,parentid,order):
        self.json_data=requests.post(self.creat_url,headers=self.headers,params={"access_token":WeWork.get_token()},json={
            "name": name,
            "parentid": parentid,
            "order": order,
            "id": None
        }
        # ,
        # # proxies=self.proxies,verify=False
                          )\
            .json()
        self.verbose(self.json_data)
        return self.json_data
    def delete(self,id =None):
        self.json_data =requests.get(self.delete_url,params={"access_token":WeWork.get_token(),
                                                    "id":id}).json()
        self.verbose(self.json_data)
        return self.json_data
    def update(self,id,name,parentid,order):
        self.json_data =requests.post(self.update_url,headers =self.headers,params={"access_token":WeWork.get_token()},
                      json={

                              "id": id,
                              "name": name,
                              "parentid": parentid,
                              "order": order

                      }).json()
        self.verbose(self.json_data)
        return self.json_data