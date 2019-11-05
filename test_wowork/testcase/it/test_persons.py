from test_wowork.api.persons import PerSons


class TestPersons:
    person = PerSons()
    def test_getpersons(self):
        userid ="WuMingHui"
        r = self.person.get_department_persons(userid)
        assert r["errcode"] == 0
        assert userid ==r["userid"]

