import requests

from test_wowork.api.base_api import BaseApi
from test_wowork.api.wework import WeWork


class SuCai(BaseApi):
    media_id_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload"
    def get_media_id(self,file_path,type):
        files = {'file': open(file_path, 'rb')}
        r = requests.post(self.media_id_url,files=files,params={"access_token":WeWork.get_message_token(),"type":type}
                          ).json()
        self.verbose(r)
        return r["media_id"]
