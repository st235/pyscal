from pyscal.interpreter import Interpreter

import pytest

@pytest.mark.parametrize("expr, expected", [
    ("1", 1),
    ("1+2", 3),
    ("1+2+3", 6),
    ("1+2*3", 7),
])
def test_parsingExpression_thenCorrectlyParsed(expr, expected):
    interpreter = Interpreter(expr)
    assert interpreter.expr() == expected
