from test_wowork.api.department import Department
from test_wowork.utils.Utils import Utils


class TestDeparment:
    def test_list(self):
        #list json assert
        department =Department()
        data = department.list("")
        assert data["errcode"] == 0
        assert data["department"][0]["name"] =="叮当研发中心"


