import unittest
from assertpy import *
from assertpy import add_extension
from sample.student import *
from sample.register import *
import unittest

class test_Register_PyHamcrest(unittest.TestCase):
    def setUp(self):
        register = Register([Student(2, "Krzysztof", "Kowal").returnObject(),
                             Student(42, "Jan", "Kowalski", [{"subject": "geography", "notes": []}]).returnObject(),
                             Student(55, "Kamil", "Stoszek", [{"subject": "maths", "notes": [4, 6, 2, 3.5]},
                                                              {"subject": "geography",
                                                               "notes": [1, 2, 3]}]).returnObject()])
        self.tmp = register

    def has_scholarship(self):
        if self.val < 4.5:
            self.error(f'{self.val} is less than 4.5!')
        return self

    add_extension(has_scholarship)

    def test_add_student_is_equal(self):
        assert_that(self.tmp.add_Student(12, "Jan", "Wisniewski")).is_equal_to({"id": 12, "name": "Jan", "surname": "Wisniewski", "subjects": [], "notices": []})

    def test_edit_student_is_instance_of_object(self):
        assert_that(self.tmp.edit_Student(2,None, "Janek", "Wisnia")).is_instance_of(object)

    def test_edit_student_is_iterable(self):
        assert_that(self.tmp.edit_Student(2,None, "Janek", "Wisnia")).is_iterable()

    def test_add_subject_contains_entry(self):
        assert_that(self.tmp.add_subject(2, "maths")).contains_entry({'subjects': [{'subject': 'maths', 'notes': []}]})

    def test_edit_subject_contains_value(self):
        assert_that(self.tmp.edit_subject(55, "maths", "physics")).contains_value([{'subject': 'physics', 'notes': [4, 6, 2, 3.5]}, {'subject': 'geography', 'notes': [1, 2, 3]}])

    def test_remove_subject_does_not_contain_value(self):
        assert_that(self.tmp.remove_subject(55, "maths")).does_not_contain_value([{'subject': 'maths', 'notes': [4, 6, 2, 3.5]}, {'subject': 'geography', 'notes': [1, 2, 3]}])

    def test_add_subject_does_not_contain_entry(self):
        assert_that(self.tmp.add_subject(2, "maths")).does_not_contain_entry({'subjects': [{'subject': 'physics', 'notes': []}]})

    def test_add_notes_is_not_none(self):
        assert_that(self.tmp.add_notes(55, "geography", [4,5])).is_not_none()

    def test_get_subject_average_is_close_to(self):
        assert_that(self.tmp.get_subject_average(55, "maths")).is_close_to(4, 0.5)

    def test_get_student_average_is_between(self):
        assert_that(self.tmp.get_student_average(55)).is_between(2.75,3)

    def test_get_student_average_has_scholarship(self):
        self.tmp.add_subject(2, "maths")
        self.tmp.add_notes(2, "maths", [5,5,5])
        assert_that(self.tmp.get_student_average(2)).has_scholarship()