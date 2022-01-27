from sample.register import *
from sample.student import *
import unittest

register = Register([Student(2, "Krzysztof", "Kowal").returnObject(),
                             Student(42, "Jan", "Kowalski", [{"subject": "geography", "notes": []}]).returnObject(),
                             Student(55, "Kamil", "Stoszek", [{"subject": "maths", "notes": [4, 6, 2, 3.5]},
                                                              {"subject": "geography",
                                                               "notes": [1, 2, 3]}]).returnObject()])
reg = register

def test_WithDocRegister(self):
    """
    >>> reg.add_Student(3, "Jan", "Dab")
    {"id": 3, "name": "Jan", "surname": "Dab", "subjects": [], "notices": []}
    >>> reg.edit_Student(2, None, "Maria", None)
    {"id": 2, "name": "Maria", "surname": "Kowal", "subjects": [], "notices": []}
    >>> reg.add_subject(2, "maths")
    {"id": 2, "name": "Maria", "surname": "Kowal", "subjects": ["subject": "maths", "notes": []], "notices": []}
    """





if __name__ == "__main__":
    import doctest
    doctest.testmod()