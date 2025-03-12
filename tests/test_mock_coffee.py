import json
import pytest

MOCK_NEW_COFFEE = {
    "name": "Flat White",
    "product": "Coffee",
    "ingredients": ["Espresso", "Milk"],
    "sold": 50
}

def test_get_all_coffees(client, mock_coffee_db):
    """Test GET /coffee"""
    response = client.get("/coffee")
    
    # output untuk debugging
    print("\nResponse data:", response.data)
    data = response.get_json()
    print("Parsed JSON:", data)
    print("Length:", len(data))
    
    assert response.status_code == 200
    assert len(data) == 2  # ini jumlah data kopi dari mock
    espresso = next((item for item in data if item["id"] == 1), None)
    assert espresso["name"] == "Mock Espresso"

def test_get_coffee_by_id(client, mock_coffee_db):
    """Test GET /coffee/<id>"""
    response = client.get("/coffee/1")
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Mock Espresso"

def test_create_coffee(client, mock_coffee_db):
    """Test POST /coffee"""
    response = client.post("/coffee", json=MOCK_NEW_COFFEE)
    
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Flat White"
# karna data nambah 1 setelah create new, jadi harusnya ada 3. klo data awal mock nya ada 2 di conftest
    assert data["id"] == 3

def test_update_coffee(client, mock_coffee_db):
    """Test PUT /coffee/<id>"""
    updated_data = {"name": "Updated Coffee"}
    response = client.put("/coffee/1", json=updated_data)
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Updated Coffee"
    assert data["product"] == "Strong COFFEE" 

def test_delete_coffee(client, mock_coffee_db):
    """Test DELETE /coffee/<id>"""
    response = client.delete("/coffee/1")
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Coffee deleted successfully"