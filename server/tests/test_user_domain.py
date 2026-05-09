from src.domain.user import User
import pytest

def test_user_creation_with_valid_email():
    """Test that a user can be created with a valid email address."""
    user = User(
        id="123e4567-e89b-12d3-a456-426614174000",
        email="dev@example.com",
        password_hash="hashed_password",
        display_name="Developer"
    )
    assert user.email == "dev@example.com"
    assert user.display_name == "Developer"

def test_user_creation_with_invalid_email_fails():
    """Test that creating a user with an invalid email raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid email format"):
        User(
            id="123e4567-e89b-12d3-a456-426614174000",
            email="invalid-email",
            password_hash="hashed_password",
            display_name="Developer"
        )
