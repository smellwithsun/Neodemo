import pytest

from test_wowork.api.department import Department
from test_wowork.utils.Utils import Utils


class TestDeparment:
    department = Department()
    exist = False
    delete_id = None
    def test_list(self):
        #list json assert
        data = self.department.list("")
        assert data["errcode"] == 0
        assert data["department"][0]["name"] =="叮当研发中心"
    @pytest.mark.parametrize("name",["dsd","djsd","dds","你大爷的dsd"])
    def test_creat(self,name):
        data =self.department.creat(name,2,10000)
        assert data["errcode"] ==0
        assert data["id"] !=None
        for depr in self.department.list("")["department"]:
            if data["id"] == depr["id"]:
                self.exist = True
        assert self.exist == True
    def test_update(self):
        data = self.department.update(5,"啦啦啦啦啦",2,10000)
        assert data["errcode"] == 0
        for depr in self.department.list("")["department"]:
            if depr["name"] == "啦啦啦啦啦":
                self.exist = True
        assert self.exist == True

    def test_delete(self):
        self.delete_id = 5
        data = self.department.delete(self.delete_id)
        assert data["errcode"] ==0
        for depr in self.department.list("")["department"]:
            if self.delete_id not in depr:
                self.exist = True
        assert self.exist ==True





