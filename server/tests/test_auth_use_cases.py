import pytest
from unittest.mock import AsyncMock
from src.application.auth.use_cases import RegisterUseCase
from src.domain.user_repository import UserRepository
from src.domain.user import User

@pytest.mark.asyncio
async def test_register_user_success():
    # Arrange
    mock_repo = AsyncMock(spec=UserRepository)
    mock_import_repo = AsyncMock(spec=UserRepository)
    mock_repo.get_by_email.return_value = None
    
    use_case = RegisterUseCase(user_repository=mock_repo)
    
    user_data = {
        "email": "test@example.com",
        "password": "securepassword123",
        "display_name": "Test User"
    }

    # Act
    user = await use_case.execute(user_data)

    # Assert
    assert user.email == "test@example.com"
    assert user.display_name == "Test User"
    mock_repo.save.assert_called_once()

@pytest.mark.asyncio
async def test_register_user_email_already_exists_fails():
    # Arrange
    mock_repo = AsyncMock(spec=UserRepository)
    existing_user = User(
        id="some-id",
        email="test@example.com",
        password_hash="hash",
        display_name="Existing"
    )
    mock_repo.get_by_email.return_value = existing_user
    
    use_case = RegisterUseCase(user_repository=mock_repo)
    
    user_data = {
        "email": "test@example.com",
        "password": "password123",
        "display_name": "New User"
    }

    # Act & Assert
    with pytest.raises(ValueError, match="Email already in use"):
        await use_case.execute(user_data)
