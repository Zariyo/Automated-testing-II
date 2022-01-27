

class Student:
    def __init__(self, studid, name, surname, subjects=None, notices=None):
        if notices is None:
            notices = []
        if subjects is None:
            subjects = []
        self.id = studid
        self.name = name
        self.surname = surname
        self.subjects = subjects
        self.notices = notices

    def returnObject(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "subjects": self.subjects, "notices": self.notices}