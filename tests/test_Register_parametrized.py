from parameterized import parameterized, parameterized_class
from sample.register import *
from sample.student import *
import unittest

class TestAgeCalc(unittest.TestCase):
    def setUp(self):
        register = Register([Student(2, "Krzysztof", "Kowal").returnObject(),
                             Student(42, "Jan", "Kowalski", [{"subject": "geography", "notes": []}]).returnObject(),
                             Student(55, "Kamil", "Stoszek", [{"subject": "maths", "notes": [4, 6, 2, 3.5]},
                                                              {"subject": "geography",
                                                               "notes": [1, 2, 3]}]).returnObject()])
        self.tmp = register

    @parameterized.expand([
        (10, "Adam", "Janowski", {"id": 10, "name": "Adam", "surname": "Janowski", "subjects": [], "notices": []}),
        (11, "Jan", "Adamowski", {"id": 11, "name": "Jan", "surname": "Adamowski", "subjects": [], "notices": []}),
        (13, "Przemyslaw", "Piotrowski", {"id": 13, "name": "Przemyslaw", "surname": "Piotrowski", "subjects": [], "notices": []}),
        (14, "Piotr", "Przemyslowski", {"id": 14, "name": "Piotr", "surname": "Przemyslowski", "subjects": [], "notices": []})
    ])

    def test_parametrized_add_student(self, studId, studName, studSurname, expectedOutput):
        self.assertEqual(self.tmp.add_Student(studId, studName, studSurname), expectedOutput)

    @parameterized.expand([
        ("ab", "Adam", "Janowski"),
        ({}, "Jan", "Adamowski"),
        ([], "Przemyslaw", "Piotrowski"),
        (None, "Piotr", "Przemyslowski")
    ])

    def test_parametrized_add_student_exceptions_bad_id(self, studId, studName, studSurname):
        self.assertRaises(ValueError, self.tmp.add_Student,studId, studName, studSurname)

    @parameterized.expand([
        ("2", None, "Krzysiu", "Kowalski", {"id": 2, "name": "Krzysiu", "surname": "Kowalski", "subjects": [], "notices": []}),
        (42, 43, "Janek", "Kowal", {"id": 43, "name": "Janek", "surname": "Kowal", "subjects": [{'notes': [], 'subject': 'geography'}], "notices": []}),
        (55, None, None, "Stoch", {"id": 55, "name": "Kamil", "surname": "Stoch", "subjects": [{'notes': [4, 6, 2, 3.5], 'subject': 'maths'},
              {'notes': [1, 2, 3], 'subject': 'geography'}], "notices": []})
    ])

    def test_parametrized_edit_student(self, studId, updId, updName, updSurname, expectedOutput):
        self.assertEqual(self.tmp.edit_Student(studId, updId, updName, updSurname), expectedOutput)

    @parameterized.expand([
        ("2", None, 12, "Kowalski"),
        (None, 43, "Janek", "Kowal"),
        (55, None, None, {"Stoch"})
    ])

    def test_parametrized_edit_student_exceptions(self, studId,updId,updName,updSurname):
        self.assertRaises(Exception, self.tmp.edit_Student, studId, updId, updName, updSurname)

    @parameterized.expand([
        (2, "maths", {"id": 2, "name": "Krzysztof", "surname": "Kowal", "subjects": [{"subject": "maths", "notes": []}], "notices": []}),
        (2, "geography", {"id": 2, "name": "Krzysztof", "surname": "Kowal", "subjects": [{"subject": "geography", "notes": []}], "notices": []}),
        (42, "maths", {"id": 42, "name": "Jan", "surname": "Kowalski", "subjects": [{"subject": "geography", "notes": []}, {"subject": "maths", "notes": []}], "notices": []}),
        (55, "physics", {"id": 55, "name": "Kamil", "surname": "Stoszek", "subjects": [{"subject": "maths", "notes": [4,6,2,3.5]},{'notes': [1, 2, 3], 'subject': 'geography'}, {"subject": "physics", "notes": []}], "notices": []}),
        (2, "arts", {"id": 2, "name": "Krzysztof", "surname": "Kowal", "subjects": [{"subject": "arts", "notes": []}], "notices": []})
    ])

    def test_parametrized_add_subject(self, studId, subject, expectedOutput):
        self.assertEqual(self.tmp.add_subject(studId, subject), expectedOutput)

    @parameterized.expand([
        ("2", "football"),
        (None, "maths"),
        (2, 12)
    ])

    def test_parametrized_add_subject_exceptions(self, studId, subject):
        self.assertRaises(Exception, self.tmp.add_subject, studId, subject)