import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test."""
    # Store original state
    original_activities = copy.deepcopy(activities)
    
    # Yield to run the test
    yield
    
    # Restore original state after test
    activities.clear()
    activities.update(original_activities)
