import pytest

from Scripts import myscript


def test_input():
    assert myscript.check_input() == "1"


