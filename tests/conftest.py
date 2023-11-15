import pytest


@pytest.fixture(scope="session")
def custom_fixture():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
