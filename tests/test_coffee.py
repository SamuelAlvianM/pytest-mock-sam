import json



def test_get_all_coffees(client):
    response = client.get("/coffee")
    assert response.status_code == 200
    assert isinstance(response.json, list)



def test_get_coffee(client):
    response = client.get("/coffee/1")
    assert response.status_code == 200
    assert "name" in response.json
    assert "ingredients" in response.json



def test_create_coffee(client):
    new_coffee = {
        "name": "Flat White",
        "product": "Coffee",
        "ingredients": ["Espresso", "Milk"],
        "sold": 50
    }
    response = client.post("/coffee", data=json.dumps(new_coffee), content_type="application/json")
    assert response.status_code == 201
    assert response.json["name"] == "Flat White"



def test_update_coffee(client):
    update_data = {"sold": 100}
    response = client.put("/coffee/1", data=json.dumps(update_data), content_type="application/json")
    assert response.status_code == 200
    assert response.json["sold"] == 100



def test_delete_coffee(client):
    response = client.delete("/coffee/1")
    assert response.status_code == 200
    assert response.json["message"] == "Coffee deleted successfully"
