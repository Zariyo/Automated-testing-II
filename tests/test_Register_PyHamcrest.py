import unittest
from hamcrest import *
from sample.register import *
from sample.student import *
import unittest

class test_Register_PyHamcrest(unittest.TestCase):
    def setUp(self):
        register = Register([Student(2, "Krzysztof", "Kowal").returnObject(),
                             Student(42, "Jan", "Kowalski", [{"subject": "geography", "notes": []}]).returnObject(),
                             Student(55, "Kamil", "Stoszek", [{"subject": "maths", "notes": [4, 6, 2, 3.5]},
                                                              {"subject": "geography",
                                                               "notes": [1, 2, 3]}]).returnObject()])
        self.tmp = register

    def test_add_student_equals(self):
        assert_that(self.tmp.add_Student(1, 'Adam', 'Kowal'), equal_to({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": [], "notices": []}))

    def test_edit_student_is_object(self):
        assert_that(self.tmp.edit_Student(2, 15, "Karol", "Wojtylski"), is_(object))

    def test_add_subject_has_entry(self):
        assert_that(self.tmp.add_subject(2, "maths"), has_entry("subjects", [{"subject": "maths", "notes": []}]))

    def test_add_notes_has_value(self):
        assert_that(self.tmp.add_notes(42, "geography", [1,2,3,4]), has_value([{'subject': 'geography', 'notes': [1, 2, 3, 4]}]))

    def test_add_behavior_notice_not_None(self):
        assert_that(self.tmp.add_behavior_notice(2, "Bad language"), not_none())

    def test_edit_subject_exception_subject_not_taught(self):
        assert_that(calling(self.tmp.edit_subject).with_args(2, "maths", "german"), raises(Exception))

    def test_get_subject_average_close_to(self):
        assert_that(self.tmp.get_subject_average(55, "maths"), close_to(4, 2))

    def test_get_student_average_less_than(self):
        assert_that(self.tmp.get_student_average(55), less_than(3))

    def test_remove_student_has_length(self):
        length = len(self.tmp.get_allStudents())
        self.tmp.remove_Student(55)
        assert_that(self.tmp.get_allStudents(), has_length(length-1))

    def test_edit_notes_has_key_all_of(self):
        assert_that(self.tmp.edit_notes(55, "geography", [4,5,5]), all_of(has_key("subjects"), has_value([{'subject': 'maths', 'notes': [4, 6, 2, 3.5]}, {'subject': 'geography', 'notes': [4, 5, 5]}])))