import pytest


@pytest.mark.dependency
def test_dependency_mark():
    assert True
