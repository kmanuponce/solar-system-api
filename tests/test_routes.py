# get all planets and return no records 
def test_get_all_planets_with_no_records(client):
    # Act 
    response = client.get("/planets")
    response_body = response.get_json() 

    # Assert 
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets(client, two_saved_planets):
    # Act 
    response = client.get("/planets")
    response_body = response.get_json() 

    # Assert 
    assert response.status_code == 200
    assert response_body[0]["name"] == "Venus"

# get one planet by id 
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "Goddess of love and beauty",
        "founder": "Heidi and Manu"
    }

# get one planet by id with no fixture
def test_get_one_planet_no_fixture(client): 
    # Act 
    planet_id = 1
    response = client.get(f"/planets/{planet_id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404 
    assert response_body["message"] == f"Planet with id {planet_id} was not found"

def test_create_one_planet(client, planet_data): 
    response = client.post("/planets", json=planet_data)
    response_body = response.get_json() 

    assert response.status_code == 201 
    assert response_body["message"] == f"Planet {planet_data['name']} successfully created"  

