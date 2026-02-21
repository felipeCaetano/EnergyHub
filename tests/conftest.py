import pytest
from fastapi.testclient import TestClient

from energyhub.app import app


@pytest.fixture
def client():
    return TestClient(app)
