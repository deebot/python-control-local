import pytest

from python_controls_local import greet


def test_greeting():
    assert greet("developer") == "Hello, developer!"


@pytest.mark.parametrize("name", ["", "   "])
def test_empty_names_are_rejected(name):
    with pytest.raises(ValueError, match="Name must not be empty"):
        greet(name)
