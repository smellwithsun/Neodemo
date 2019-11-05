import requests

from test_wowork.api.base_api import BaseApi
from test_wowork.api.sucai import SuCai
from test_wowork.api.wework import WeWork


class Message(BaseApi):
    send_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
    def send_text(self,msg=None,users=[],parties=[],tags=[]):
        self.json_data=requests.post(self.send_url,params={"access_token":WeWork.get_message_token()},
                      json={
                          "touser": "|".join(users),
                          "toparty": "|".join(parties),
                          "totag": "|".join(tags),
                          "msgtype": "text",
                          "agentid": WeWork.agent_id,
                          "text": {
                              "content": msg
                          },
                          "safe": 0,
                          "enable_id_trans": 0
                      }).json()
        self.verbose()
        return self.json_data
    def send_voice(self, path, users=[], parties=[], tags=[]):
        sucai = SuCai()
        self.json_data = requests.post(self.send_url, params={"access_token": WeWork.get_message_token()},
                                       json={
                                           "touser": "|".join(users),
                                           "toparty": "|".join(parties),
                                           "totag": "|".join(tags),
                                           "msgtype": "voice",
                                           "agentid": WeWork.agent_id,
                                           "voice": {
                                               "media_id": sucai.get_media_id(path,"voice")
                                           }
                                       }).json()
        self.verbose()
        return self.json_data
        pass
    def send_picture(self,path,users=[],parties=[],tags=[]):
        sucai =SuCai()
        self.json_data = requests.post(self.send_url, params={"access_token": WeWork.get_message_token()},
                                       json={
                                           "touser": "|".join(users),
                                           "toparty": "|".join(parties),
                                           "totag": "|".join(tags),
                                           "msgtype": "image",
                                           "agentid": WeWork.agent_id,
                                           "image": {
                                               "media_id": sucai.get_media_id(path,"image")
                                           },
                                           "safe": 0
                                       }).json()
        self.verbose()
        return self.json_data
    def send_movie(self,path,users=[],parties=[],tags=[]):
        sucai =SuCai()
        self.json_data = requests.post(self.send_url, params={"access_token": WeWork.get_message_token()},
                                        json={
                                               "touser": "|".join(users),
                                           "toparty": "|".join(parties),
                                           "totag": "|".join(tags),
                                           "msgtype": "video",
                                           "agentid": WeWork.agent_id,
                                               "video" : {
                                                    "media_id" :sucai.get_media_id(path,"video") ,
                                                    "title" : "Title",
                                                   "description" : "Description"
                                               },
                                               "safe":0
                                            }).json()
        self.verbose()
        return self.json_data
    def send_file(self,path,users=[],parties=[],tags=[]):
        sucai =SuCai()
        self.json_data = requests.post(self.send_url, params={"access_token": WeWork.get_message_token()},
                                       json={
                                           "touser": "|".join(users),
                                           "toparty": "|".join(parties),
                                           "totag": "|".join(tags),
                                           "msgtype": "file",
                                           "agentid": WeWork.agent_id,
                                           "file" : {
                                            "media_id" : sucai.get_media_id(path,"file")
                                           },
                                           "safe":0
                                        }).json()
        self.verbose()
        return self.json_data
    def send_file_card(self,dec,title,users=[],parties=[],tags=[]):
        self.json_data = requests.post(self.send_url, params={"access_token": WeWork.get_message_token()},
                                       json={
                                           "touser": "|".join(users),
                                           "toparty": "|".join(parties),
                                           "totag": "|".join(tags),
                                           "msgtype": "news",
                                           "agentid": WeWork.agent_id,
                                           "news": {
                                               "articles": [
                                                   {
                                                       "title": title,
                                                       "description": dec,
                                                       "url": "URL",
                                                       "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
                                                   }
                                               ]
                                           },
                                           "enable_id_trans": 0
                                       }).json()
        self.verbose()
        return self.json_data
    def send_task_card(self,task_id,users=[],parties=[],tags=[]):
        self.json_data = requests.post(self.send_url, params={"access_token": WeWork.get_message_token()},
                                       json={
                                           "touser": "|".join(users),
                                           "toparty": "|".join(parties),
                                           "totag": "|".join(tags),
                                           "msgtype" : "taskcard",
                                           "agentid" : WeWork.agent_id,
                                           "taskcard" : {
                                                    "title" : "赵明登的礼物申请",
                                                    "description" : "礼品：A31茶具套装<br>用途：赠与小黑科技张总经理",
                                                    "url" : "https:www.baidu.com",
                                                    "task_id" : task_id,
                                                    "btn":[
                                                        {
                                                            "key": "key111",
                                                            "name": "批准",
                                                            "replace_name": "已批准",
                                                            "color":"red",
                                                            "is_bold": True
                                                        },
                                                        {
                                                            "key": "key222",
                                                            "name": "驳回",
                                                            "replace_name": "已驳回"
                                                        }
                                                    ]
                                           },
                                           "enable_id_trans": 0
                                        }).json()
        self.verbose()
        return self.json_data