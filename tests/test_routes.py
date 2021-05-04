# get all books and return no records 
def test_get_all_books_with_no_records(client):
    # Act 
    response = client.get("/planets")
    response_body = response.get_json() 

    # Assert 
    assert response.status_code == 200
    assert response_body == []