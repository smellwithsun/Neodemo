import requests

from test_wowork.api.BaseApi import BaseApi
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
    def send_voice(self):
        pass
    def send_picture(self):
        pass