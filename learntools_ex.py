from learntools.core import *
import pandas as pd, numpy as np

ex1_sol = 5
ex2_sol = "UPPERCASE"
ex3_sol = [3, 2, 1]
ex4_sol = pd.Series({
        "Col1" : 6,
        "Col2" : 6
    })
ex5_sol = np.array([1,2,3])

class Exercise1(EqualityCheckProblem):
    _solution = None
    _var = "ex1_sol"
    _expected = ex1_sol
    _hint = ("Try using your brain")

class Exercise2(EqualityCheckProblem):
    _solution = None
    _var = "ex2_sol"
    _expected = ex2_sol
    _hint = ("Try using your brain")

class Exercise3(EqualityCheckProblem):
    _solution = None
    _var = "ex3_sol"
    _expected = ex3_sol
    _hint = ("Try using your brain")

class Exercise4(EqualityCheckProblem):
    _solution = None
    _var = "ex4_sol"
    _expected = ex4_sol
    _hint = ("Try using your brain")

class Exercise5(EqualityCheckProblem):
    _solution = None
    _var = "ex5_sol"
    _expected = ex5_sol
    _hint = ("Try using your brain")

qvars = bind_exercises(globals(), [
    Exercise1,
    Exercise2,
    Exercise3,
    Exercise4,
    Exercise5
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)