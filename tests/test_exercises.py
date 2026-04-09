# tests/test_exercises.py
import exercises


def test_rectangle_perimeter():
    assert exercises.rectangle_perimeter(7, 3) == 20


def test_reverse_variables():
    a, b = exercises.reverse_variables("happy", "always")
    assert a == "always"
    assert b == "happy"


def test_total_and_average():
    total, avg = exercises.total_and_average(90, 80, 77)
    assert total == 247
    assert abs(avg - (247 / 3)) < 0.0001


def test_last_digit():
    assert exercises.last_digit(47839) == 9


def test_is_divisible():
    assert exercises.is_divisible(35728, 1033) is False


def test_constant_string():
    assert exercises.CONSTANT_STRING == "Python Programming"