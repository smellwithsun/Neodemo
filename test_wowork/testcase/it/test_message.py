from test_wowork.api.message import Message


class TestMessage:
    message = Message()
    def test_text(self):
        data =self.message.send_text("你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。",
                                     ["WuMingHui"])
        assert data['errcode'] == 0
        assert data["errmsg"] == 'ok'
        assert data['invaliduser'] == ''
    def test_picture(self):
        data =self.message.send_picture("/Users/neo/Desktop/1.jpg",["WuMingHui"])
        assert data['errcode'] == 0
        assert data["errmsg"] == 'ok'
    def test_voice(self):
        data =self.message.send_voice("/Users/neo/Desktop/2.AMR",["WuMingHui"])
        assert data['errcode'] == 0
        assert data["errmsg"] == 'ok'
    def test_file(self):
        data =self.message.send_file("/Users/neo/Desktop/1.txt",["WuMingHui"])
        assert data['errcode'] == 0
        assert data["errmsg"] == 'ok'

    def test_movie(self):
        data = self.message.send_movie("/Users/neo/Desktop/4.mp4", ["WuMingHui"])
        assert data['errcode'] == 0
        assert data["errmsg"] == 'ok'

    def test_file_card(self):
        data = self.message.send_file_card("啦啦啦啦","lallall",["WuMingHui"])
        assert data['errcode'] == 0
        assert data["errmsg"] == 'ok'
    def test_task_card(self):
        data = self.message.send_task_card("ssa223",["WuMingHui"])
        assert data['errcode'] == 0
        assert data["errmsg"] == 'ok'







