import pytest

@pytest.fixture
def temporary_user():
    user = {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "is_active": True}
    yield user
    print("\n--- Teardown: Cleaning up temporary user data ---")

def test_user_is_active(temporary_user):
    assert temporary_user["is_active"] == True
    assert temporary_user["id"] == 1