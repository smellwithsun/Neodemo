from test_wowork.api.sucai import SuCai


class TestSucai:
    sucai =SuCai()
    def test_get_media_id(self):
        data =self.sucai.get_media_id("/Users/neo/Desktop/1.jpg")
        assert data is not None



