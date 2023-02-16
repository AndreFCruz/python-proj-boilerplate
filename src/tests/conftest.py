"""Common pytest fixtures to be used in different tests.

NOTE: file name must be "conftest.py" to enable sharing fixtures across multiple
files.

Pytest reference:
https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files
"""

import pytest
import numpy as np


@pytest.fixture(params=[23, 42])
def random_seed(request) -> int:
    """Example of a fixture that can take multiple values for all tests."""
    return request.param


@pytest.fixture
def rng(random_seed) -> np.random.Generator:
    return np.random.default_rng(random_seed)
