import pytest
from flask import Flask
import sys
from unittest.mock import patch
import importlib

# buat test per sesi, jadi kita gaakan bisa run test secara overall. harus by file
@pytest.fixture(scope="session", autouse=True)
def setup_mock_environment():
    # data Mock ditulis disini
    mock_data = {
        1: {"name": "Mock Espresso", "id": 1, "product": "Strong COFFEE", "ingredients": ["Coffee Beans", "Water"], "sold": 100},
        2: {"name": "Mock Latte", "id": 2, "product": "Milk COFFEE", "ingredients": ["Coffee Beans", "Milk", "Water"], "sold": 80}
    }
    
    # simpan data mock menggantikan coffee_db
    if 'model.coffee_model' in sys.modules:
        original_module = sys.modules['model.coffee_model']
        original_module.coffee_db = mock_data
    else:

        import types
        mock_module = types.ModuleType('coffee_model')
        mock_module.coffee_db = mock_data
        sys.modules['model.coffee_model'] = mock_module
    
    if 'routes.coffee_service' in sys.modules:
        importlib.reload(sys.modules['routes.coffee_service'])
    
    yield

@pytest.fixture
def app():
    """Create a Flask app for testing."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    
    from routes.coffee_service import coffee_blueprint
    app.register_blueprint(coffee_blueprint)
    
    return app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def mock_coffee_db():
    """Mock the coffee_db for individual tests.
    This is mainly for test functions to access the mock data."""

    mock_data = {
        1: {"name": "Mock Espresso", "id": 1, "product": "Strong COFFEE", "ingredients": ["Coffee Beans", "Water"], "sold": 100},
        2: {"name": "Mock Latte", "id": 2, "product": "Milk COFFEE", "ingredients": ["Coffee Beans", "Milk", "Water"], "sold": 80}
    }
    yield mock_data