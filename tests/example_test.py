import pytest

@pytest.fixture
def example_fixture():
    return 1 + 1

def test_with_fixture(example_fixture):
    assert example_fixture == 2
