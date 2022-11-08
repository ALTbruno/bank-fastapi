from fastapi.testclient import TestClient

def test_get_all_accounts(client: TestClient):
    response = client.get("/api/accounts")
    content = response.json()
    assert response.status_code == 200
    assert isinstance(content, list)

def test_get_account_by_id(client: TestClient):
    response = client.get("/api/accounts/6358230884b46f45777e8ff2")
    assert response.status_code == 200

def test_get_account_balance(client: TestClient):
    response = client.get("/api/accounts/6358230884b46f45777e8ff2/balance")
    assert response.status_code == 200

def test_transfer(client: TestClient):
    origin_account_id = "635944c11a0bec8db008c472"
    body = {
	'destination_account_id': '6358230884b46f45777e8ff2',
	'value_in_cents': 499
    }
    response = client.post(f"/api/accounts/{origin_account_id}/transfer", json=body)
    content = response.json()
    assert content['origin_account_id'] == origin_account_id
    assert content['destination_account_id'] == body['destination_account_id']
    assert content['value_in_cents'] == str(body['value_in_cents'])
    assert response.status_code == 201

def test_transfer_with_destination_same_as_origin(client: TestClient):
    origin_account_id = "635944c11a0bec8db008c472"
    body = {
	'destination_account_id': origin_account_id,
	'value_in_cents': 499
    }
    response = client.post(f"/api/accounts/{origin_account_id}/transfer", json=body)
    content = response.json()
    assert response.status_code == 400
    assert content['message'] == "destination_account_id must be different from origin_account_id"

def test_transfer_with_insufficient_balance(client: TestClient):
    origin_account_id = "635944c11a0bec8db008c472"
    body = {
	'destination_account_id': '6358230884b46f45777e8ff2',
	'value_in_cents': 500000
    }
    response = client.post(f"/api/accounts/{origin_account_id}/transfer", json=body)
    content = response.json()
    assert response.status_code == 400
    assert content['message'] == "Insufficient balance"

def test_get_account_transfers(client: TestClient):
    account_id = "635944c11a0bec8db008c472"
    response = client.get(f"/api/accounts/{account_id}/transactions")
    content = response.json()
    assert response.status_code == 200
    assert isinstance(content, list)

def test_get_account_transfers_with_date_filter(client: TestClient):
    account_id = "635944c11a0bec8db008c472"
    start_date = "2022-10-01"
    end_date = "2022-10-26"
    response = client.get(f"/api/accounts/{account_id}/transactions?start_date={start_date}&end_date={end_date}")
    content = response.json()
    assert response.status_code == 200
    assert isinstance(content, list)

def test_get_account_transfers_with_invalid_date_filter(client: TestClient):
    account_id = "635944c11a0bec8db008c472"
    start_date = "01-10-2022"
    end_date = "26-10-2022"
    response = client.get(f"/api/accounts/{account_id}/transactions?start_date={start_date}&end_date={end_date}")
    content = response.json()
    assert response.status_code == 400
    assert content['message'] == "Date format must be yyyy-MM-dd"
