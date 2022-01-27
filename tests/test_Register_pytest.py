from parameterized import parameterized, parameterized_class
from sample.register import *
from sample.student import *
import unittest
import pytest


register = Register([Student(2, "Krzysztof", "Kowal").returnObject(),
                             Student(42, "Jan", "Kowalski", [{"subject": "geography", "notes": []}]).returnObject(),
                             Student(55, "Kamil", "Stoszek", [{"subject": "maths", "notes": [4, 6, 2, 3.5]},
                                                              {"subject": "geography",
                                                               "notes": [1, 2, 3]}]).returnObject()])
reg = register

def test_add_student():
    assert reg.add_Student(3, "Ewa", "Robak") == {"id": 3, "name": "Ewa", "surname": "Robak", "subjects": [], "notices": []}

def test_add_student_exception():
    with pytest.raises(Exception):
        reg.add_Student("ab", "Jan", "Robak")

def test_edit_student():
    assert reg.edit_Student(2, None, "Patryk", None) == {"id": 2, "name": "Patryk", "surname": "Kowal", "subjects": [], "notices": []}

def test_edit_student_exception():
    with pytest.raises(Exception):
        reg.edit_Student(2, None, 12, None)

def test_remove_student():
    assert reg.remove_Student(2) == {"id": 2, "name": "Patryk", "surname": "Kowal", "subjects": [], "notices": []}

def test_remove_student_exception():
    with pytest.raises(Exception):
        reg.remove_Student("O")

def test_add_subject():
    assert reg.add_subject(42, "maths") == {"id": 42, "name": "Jan", "surname": "Kowalski", "subjects": [{"subject": "geography", "notes": []}, {"subject": "maths", "notes": []}], "notices": []}

def test_add_subject_exception():
    with pytest.raises(Exception):
        reg.add_subject(28, "mathematics")

def test_get_student_average():
    assert reg.get_student_average(55) == 2.94

def test_get_student_average_exception():
    with pytest.raises(Exception):
        reg.get_student_average(102)