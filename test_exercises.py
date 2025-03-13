import pytest

from exercises import exercise_1, exercise_2, exercise_3, exercise_4, exercise_5

def test_exercise_1():
    assert exercise_1(2, 3) == 5  # Example test case

def test_exercise_2():
    assert exercise_2("hello") == "HELLO"  # Modify accordingly

def test_exercise_3():
    assert exercise_3([1, 2, 3]) == [3, 2, 1]  # Example case

def test_exercise_4():
    assert exercise_4(10) == 100  # Modify accordingly

def test_exercise_5():
    assert exercise_5("test") == "tset"  # Modify accordingly
