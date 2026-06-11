from pyscal.interpreter import Interpreter

import pytest

@pytest.mark.parametrize("expr, expected", [
    ("1", 1),
    ("1+2", 3),
    ("1+2+3", 6),
    ("1+2*3", 7),
    ("1+2+3+4+5", 15),
    ("1+2*3-1", 6),
    ("(1+2)*3", 9),
    ("21/(1+2*3)", 3),
])
def test_parsingExpression_thenCorrectlyParsed(expr, expected):
    interpreter = Interpreter(expr)
    assert interpreter.interpret() == expected
