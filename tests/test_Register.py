from sample.register import *
from sample.student import *
import unittest


class test_Register(unittest.TestCase):

    def setUp(self):
        register = Register([Student(2, "Krzysztof", "Kowal").returnObject(),
                             Student(42, "Jan", "Kowalski", [{"subject": "geography", "notes": []}]).returnObject(),
                             Student(55, "Kamil", "Stoszek", [{"subject": "maths", "notes": [4, 6, 2, 3.5]},
                                                              {"subject": "geography",
                                                               "notes": [1, 2, 3]}]).returnObject()])
        self.tmp = register

    def test_add_Student(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": [], "notices": []},
                         self.tmp.add_Student(1, 'Adam', 'Kowal'))

    def test_add_Student_exception_studentExists(self):
        self.assertRaises(Exception, self.tmp.add_Student, 2, 'Krzysztof', 'Kowal')

    def test_add_Student_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.add_Student, "abc", 'Adam', 'Nowak')

    def test_add_Student_id_as_float(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": [], "notices": []},
                         self.tmp.add_Student(1.0, 'Adam', 'Kowal'))

    def test_add_Student_id_as_string(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": [], "notices": []},
                         self.tmp.add_Student("1.0", 'Adam', 'Kowal'))

    def test_add_Student_exception_id_as_None(self):
        self.assertRaises(ValueError, self.tmp.add_Student, None, 'Adam', 'Nowak')

    def test_add_Student_exception_id_as_empty_list(self):
        self.assertRaises(ValueError, self.tmp.add_Student, [], 'Adam', 'Nowak')

    def test_add_Student_exception_id_as_empty_object(self):
        self.assertRaises(ValueError, self.tmp.add_Student, {}, 'Adam', 'Nowak')

    def test_add_Student_exception_name_not_string(self):
        self.assertRaises(TypeError, self.tmp.add_Student, 4, 15, 'Nowak')

    def test_add_Student_exception_surname_not_string(self):
        self.assertRaises(TypeError, self.tmp.add_Student, 4, 'Adam', 20)

    def test_edit_Student(self):
        self.assertEqual({"id": 2, "name": "Krzysiek", "surname": "Kowalski", "subjects": [], "notices": []},
                         self.tmp.edit_Student(2, None, "Krzysiek", "Kowalski"))

    def test_edit_Student_exception_noStudent(self):
        self.assertRaises(Exception, self.tmp.edit_Student, 15, None, "Adam", "Kamien")

    def test_edit_Student_exception_id_not_int(self):
        self.assertRaises(Exception, self.tmp.edit_Student, "abc", None, "Adam", "Kamien")

    def test_edit_Student_exception_id_as_empty_list(self):
        self.assertRaises(ValueError, self.tmp.edit_Student, 15, [], "Adam", "Kamien")

    def test_edit_Student_exception_id_as_empty_object(self):
        self.assertRaises(ValueError, self.tmp.edit_Student, 15, {}, "Adam", "Kamien")

    def test_edit_Student_exception_name_not_string(self):
        self.assertRaises(TypeError, self.tmp.edit_Student, 15, None, 123, "Kamien")

    def test_edit_Student_exception_surname_not_string(self):
        self.assertRaises(TypeError, self.tmp.edit_Student, 15, None, "Adam", 123)

    def test_remove_Student(self):
        self.tmp.add_Student(28, 'Adam', 'Nowak')
        self.assertEqual({"id": 28, "name": "Adam", "surname": "Nowak", "subjects": [], "notices": []}, self.tmp.remove_Student(28))

    def test_remove_Student_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.remove_Student, "abc")

    def test_remove_Student_no_student(self):
        self.assertRaises(Exception, self.tmp.remove_Student, 100)

    def test_add_subject(self):
        self.assertEqual(
            {"id": 2, "name": "Krzysztof", "surname": "Kowal", "subjects": [{"subject": "maths", "notes": []}], "notices": []},
            self.tmp.add_subject(2, "maths"))

    def test_add_subject_exception_no_subject(self):
        self.assertRaises(Exception, self.tmp.add_subject, 2, "spanish")

    def test_add_subject_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.add_subject, "abc", "maths")

    def test_edit_subject(self):
        self.assertEqual(
            {"id": 42, "name": "Jan", "surname": "Kowalski", "subjects": [{"subject": "maths", "notes": []}], "notices": []},
            self.tmp.edit_subject(42, "geography", "maths"))

    def test_edit_subject_exception_no_subject(self):
        self.assertRaises(Exception, self.tmp.add_subject, 2, "spanish", "maths")

    def test_edit_subject_exception_id_not_int(self):
        self.assertRaises(Exception, self.tmp.add_subject, "abc", "geography", "maths")

    def test_edit_subject_exception_no_subject_update(self):
        self.assertRaises(Exception, self.tmp.add_subject, 2, "geography", "spanish")

    def test_remove_subject(self):
        self.assertEqual(
            {"id": 42, "name": "Jan", "surname": "Kowalski", "subjects": [], "notices": []},
            self.tmp.remove_subject(42, "geography"))

    def test_remove_subject_exception_no_id(self):
        self.assertRaises(Exception, self.tmp.remove_subject, 254, "geography")

    def test_remove_subject_exception_id_not_int(self):
        self.assertRaises(Exception, self.tmp.remove_subject, "abc", "geography")

    def test_remove_subject_exception_no_subject(self):
        self.assertRaises(Exception, self.tmp.remove_subject, 42, "maths")

    def test_add_notes_single_note(self):
        self.assertEqual(
            {"id": 42, "name": "Jan", "surname": "Kowalski", "subjects": [{"subject": "geography", "notes": [5]}], "notices": []},
            self.tmp.add_notes(42, "geography", 5))

    def test_add_notes_list_of_notes(self):
        self.assertEqual(
            {"id": 42, "name": "Jan", "surname": "Kowalski", "subjects": [{"subject": "geography", "notes": [5, 5, 3]}], "notices": []},
            self.tmp.add_notes(42, "geography", [5,5,3]))

    def test_add_notes_exception_id_not_int(self):
        self.assertRaises(Exception, self.tmp.add_notes, "abc", "geography", 6)

    def test_add_notes_exception_student_no_subject(self):
        self.assertRaises(Exception, self.tmp.add_notes, 42, "maths", 6)

    def test_add_notes_exception_student_incorrect_note(self):
        self.assertRaises(ValueError, self.tmp.add_notes, 42, "geography", "b")

    def test_add_notes_exception_student_incorrect_notes(self):
        self.assertRaises(ValueError, self.tmp.add_notes, 42, "geography", [1, 3.4, 5, "a"])

    def test_add_notes_floats_as_notes(self):
        self.assertEqual(
            {"id": 42, "name": "Jan", "surname": "Kowalski",
             "subjects": [{"subject": "geography", "notes": [1, 3.40, 5.12, 4.13]}], "notices": []},
            self.tmp.add_notes(42, "geography", [1, 3.4, 5.12, 4.126]))

    def test_edit_notes(self):
        self.assertEqual(
            {"id": 55, "name": "Kamil", "surname": "Stoszek",
             "subjects": [{"subject": "maths", "notes": [2, 2.5, 3]}, {'notes': [1, 2, 3], 'subject': 'geography'}], "notices": []},
            self.tmp.edit_notes(55,'maths',[2,2.5,3])
        )

    def test_edit_notes_exception_incorrect_notes(self):
        self.assertRaises(ValueError, self.tmp.edit_notes, 55, "maths", ["b", "c"])

    def test_edit_notes_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.edit_notes, "abc", "maths", 6)

    def test_edit_notes_exception_student_no_subject(self):
        self.assertRaises(Exception, self.tmp.edit_notes, 55, "history", [1,2,3])

    def test_get_subject_average(self):
        self.assertEqual(3.88, self.tmp.get_subject_average(55, "maths"))

    def test_get_subject_average_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.get_subject_average, "abc", "maths")

    def test_get_student_average(self):
        self.assertEqual(2.94, self.tmp.get_student_average(55))

    def test_get_student_average_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.get_student_average, "abc")

    def test_add_behavior_notice(self):
        self.assertEqual({"id": 2, "name": "Krzysztof", "surname": "Kowal", "subjects": [], "notices": ["Uses bad language"]},
                         self.tmp.add_behavior_notice(2, "Uses bad language"))

    def test_add_behavior_notice_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.add_behavior_notice, "abc", "Bad language")

    def test_add_behavior_notice_exception_notice_not_string(self):
        self.assertRaises(TypeError, self.tmp.add_behavior_notice, 2, 123)

    def test_edit_behavior_notice(self):
        self.tmp.add_behavior_notice(2, "Uses bad language")
        self.assertEqual(
            {"id": 2, "name": "Krzysztof", "surname": "Kowal", "subjects": [], "notices": ["Beats his friends"]},
            self.tmp.edit_behavior_notice(2, "Uses bad language", "Beats his friends"))

    def test_edit_behavior_notice_exception_id_not_int(self):
        self.tmp.add_behavior_notice(2, "Uses bad language")
        self.assertRaises(ValueError, self.tmp.edit_behavior_notice, "abc", "Uses bad language", "Bad language")

    def test_edit_behavior_notice_exception_newNotice_not_string(self):
        self.tmp.add_behavior_notice(2, "Uses bad language")
        self.assertRaises(TypeError, self.tmp.edit_behavior_notice, 2, "Uses bad language", 123)

    def test_edit_behavior_notice_exception_oldNotice_not_string(self):
        self.tmp.add_behavior_notice(2, "Uses bad language")
        self.assertRaises(TypeError, self.tmp.edit_behavior_notice, 2, 123, "Bad language")