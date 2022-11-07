import pytest
from fastapi.testclient import TestClient
from typing import Generator
from main import app

@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
