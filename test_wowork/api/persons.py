from test_wowork.api.base_api import BaseApi
from test_wowork.api.wework import WeWork


class PerSons(BaseApi):

    def created_person(self):
        pass
    def read_person(self):
        pass
    def update_person(self):
        pass
    def delete_person(self):
        pass
    def all_delete_person(self):
        pass
    def get_department_persons(self,user_id):
        print(WeWork.get_message_token())
        get_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        return self.send_data("get",get_url,WeWork.get_message_token(),{"userid":user_id})


    def get_department_person_detail(self):
        pass
    def exchange(self):
        pass
    def two_verify(self):
        pass
    def invite_person(self):
        pass
    def get_decode(self):
        pass
