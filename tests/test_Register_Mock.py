from sample.database import *
from sample.student import *
from sample.register import *
from assertpy import *
import unittest
from unittest.mock import *


class test_Register_Mock(unittest.TestCase):

    def setUp(self):
        self.register = Register([Student(2, "Krzysztof", "Kowal").returnObject(),
                             Student(42, "Jan", "Kowalski", [{"subject": "geography", "notes": []}]).returnObject(),
                             Student(55, "Kamil", "Stoszek", [{"subject": "maths", "notes": [4, 6, 2, 3.5]},
                                                              {"subject": "geography",
                                                               "notes": [1, 2, 3]}]).returnObject(),
                             Student(10, "Kamil", "Michalski", [{"subject": "maths", "notes": []}]).returnObject()])
        self.database = Database()
        self.database.read_students = Mock(name="read_students")
        self.database.add_student = Mock(name="add_student")
        self.database.del_student = Mock(name="del_student")
        self.database.edit_student = Mock(name="edit_student")
        self.database.read_subjects = Mock(name="read_subjects")
        self.database.add_subject = Mock(name="add_subject")
        self.database.del_subject = Mock(name="del_subject")
        self.database.edit_subject = Mock(name="edit_subject")
        self.database.read_notes = Mock(name="read_notes")
        self.database.add_notes = Mock(name="add_notes")
        self.database.del_notes = Mock(name="del_notes")
        self.database.edit_notes = Mock(name="edit_notes")
        self.database.read_notices = Mock(name="read_notices")
        self.database.add_notice = Mock(name="add_notice")
        self.database.del_notice = Mock(name="del_notice")
        self.database.edit_notice = Mock(name="edit_notice")

    def get_notes_fake_mock(self):
        return [2,2,3,3.5]

    def add_student_fake_mock(self):
        return {"id": 205852, "name": "Paweł","surname": "Szendzielski", "subjects": [], "notices": []}

    def test_read_students_mock(self):
        self.assertIsInstance(self.database.read_students, Mock)

    def test_add_student_mock(self):
        self.assertIsInstance(self.database.add_student, Mock)

    def test_del_student_mock(self):
        self.assertIsInstance(self.database.del_student, Mock)

    def test_edit_student_mock(self):
        self.assertIsInstance(self.database.edit_student, Mock)

    def test_read_subjects_mock(self):
        self.assertIsInstance(self.database.read_subjects, Mock)

    def test_add_subject_mock(self):
        self.assertIsInstance(self.database.add_subject, Mock)

    def test_del_subject_mock(self):
        self.assertIsInstance(self.database.del_subject, Mock)

    def test_edit_subject_mock(self):
        self.assertIsInstance(self.database.edit_subject, Mock)

    def test_read_notes_mock(self):
        self.assertIsInstance(self.database.read_notes, Mock)

    def test_add_notes_mock(self):
        self.assertIsInstance(self.database.add_notes, Mock)

    def test_del_notes_mock(self):
        self.assertIsInstance(self.database.del_notes, Mock)

    def test_edit_notes_mock(self):
        self.assertIsInstance(self.database.edit_notes, Mock)

    def test_read_notices_mock(self):
        self.assertIsInstance(self.database.read_notices, Mock)

    def test_add_notice_mock(self):
        self.assertIsInstance(self.database.add_notice, Mock)

    def test_del_notice_mock(self):
        self.assertIsInstance(self.database.del_notice, Mock)

    def test_edit_notice_mock(self):
        self.assertIsInstance(self.database.edit_notice, Mock)

    def test_read_students_mock_return_value(self):
        self.database.read_students.return_value = [{"id": 42, "name": "Jan", "surname": "Kowalski",
                                                     "subjects": [
                                                         {"subject": "geography", "notes": [1, 3.40, 5.12, 4.13]}],
                                                     "notices": []},
                                                    {"id": 65, "name": "Karol", "surname": "Koral", "subjects": [
                                                        {"subject": "maths", "notes": [3, 2.50, 5, 4.25]}],
                                                     "notices": []}]

        self.assertEqual([{"id": 42, "name": "Jan", "surname": "Kowalski",
                           "subjects": [
                               {"subject": "geography", "notes": [1, 3.40, 5.12, 4.13]}],
                           "notices": []},
                          {"id": 65, "name": "Karol", "surname": "Koral", "subjects": [
                              {"subject": "maths", "notes": [3, 2.50, 5, 4.25]}],
                           "notices": []}], self.database.read_students())

    def test_add_student_mock_return_value(self):
        self.database.add_student.return_value = {"id": 521, "name": "Jan", "surname": "Janosik",
                           "subjects": [],
                           "notices": []}

        self.assertEqual(self.database.add_student("student"), self.register.add_Student(521, "Jan", "Janosik"))

    def test_edit_student_mock_create_autospec_typeError(self):
        x = create_autospec(self.register)
        self.assertRaises(TypeError, x.edit_Student, 15, "maths", "geography", "physics", "history")

    def test_get_notes_mock_create_autospec_typeError(self):
        x = create_autospec(self.register)
        self.assertRaises(TypeError, x.get_notes, 15)


    def test_del_student_mock_side_effect_exception(self):
        self.database.del_student.side_effect = ({"id": 42, "name": "Jan", "surname": "Kowalski",
                           "subjects": [
                               {"subject": "geography", "notes": [1, 3.40, 5.12, 4.13]}],
                           "notices": []}, Exception("Student with such id does not exist"))

        self.register.remove_Student(42)
        self.database.del_student(42)
        self.assertRaises(Exception, self.database.del_student, 42)

    def test_add_subject_mock_side_effect(self):
        self.database.add_subject(15, "maths").return_value({"id": 15, "name": "Kamil", "surname": "Kowalski",
                           "subjects": [
                               {"subject": "maths", "notes": []}],
                           "notices": []})

        assert_that(self.database.add_subject(15, "maths")).is_instance_of(object)

    def test_del_subject_mock_create_autospec_typeError(self):
        x = create_autospec(self.register)
        self.assertRaises(TypeError, x.remove_subject, 15, "maths", "adam")

    def test_add_subject_mock_create_autospec_typeError(self):
        x = create_autospec(self.register)
        self.assertRaises(TypeError, x.add_subject, 15, "maths", "adam")

    def test_add_notes_mock_return_value(self):
        self.database.add_notes.return_value = {"id": 10, "name": "Kamil", "surname": "Michalski",
                           "subjects": [
                               {"subject": "maths", "notes": [3,4,5]}],
                           "notices": []}
        self.assertEqual(self.database.add_notes(), self.register.add_notes(10, "maths", [3,4,5]))

    def test_read_notes_magic_mock(self):
        self.database.read_notes = MagicMock(return_value=[4,6,2,3.5])
        self.database.read_notes(55, "maths")
        self.database.read_notes.assert_called_with(55, "maths")

    def test_read_notices_magic_mock(self):
        self.database.read_notices = MagicMock(return_value=["Złe zachowanie."])
        self.database.read_notices(55)
        self.database.read_notices.assert_called_once()

    def test_get_student_average_magic_mock(self):
        self.register.get_student_average = MagicMock(return_value=3.2)
        self.register.get_student_average(55)
        self.register.get_student_average.assert_called_once_with(55)

    def test_del_subject(self):
        self.database.del_subject = MagicMock(return_value={"Student"})
        self.database.del_subject.assert_not_called()

    def test_add_student_fake_mock(self):
        self.assertEqual(self.add_student_fake_mock(), self.register.add_Student(205852, "Paweł", "Szendzielski"))

    def test_get_notes_fake_mock(self):
        self.register.add_Student(205852, "Paweł", "Szendzielski")
        self.register.add_subject(205852, "maths")
        self.register.add_notes(205852, "maths", [2, 2, 3, 3.5])
        self.assertEqual(self.get_notes_fake_mock(), self.register.get_notes(205852, "maths"))