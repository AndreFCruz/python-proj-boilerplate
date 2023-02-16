"""Example test module.
"""

from my_project import foo


def test_greeting():
    foo("Someone")
    assert True


def test_with_fixture(rng):
    assert 0 <= rng.random() <= 1       # always true as well
