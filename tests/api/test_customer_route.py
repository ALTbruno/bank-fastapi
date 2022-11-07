from fastapi.testclient import TestClient

def test_customer_registration(client: TestClient):
    body = {
	'name': 'Isaac',
	'last_name': 'Farias',
	'cpf': '98167244806',
	'birth_date': '1991-11-06',
	'email': 'isaac@email.com',
	'password': 'iuKGfU0qJ1'
    }

    response = client.post("/api/customers", json=body)
    assert response.status_code == 201

def test_customer_registration_with_blank_values(client: TestClient):
    body = {
	'name': '',
	'last_name': '',
	'cpf': '',
	'birth_date': '',
	'email': '',
	'password': ''
    }

    response = client.post("/api/customers", json=body)
    assert response.status_code == 422

def test_customer_registration_with_birth_date_invalid_format(client: TestClient):
    body = {
	'name': 'Isaac',
	'last_name': 'Farias',
	'cpf': '98167244807',
	'birth_date': '06-11-1991',
	'email': 'isaac.farias@email.com',
	'password': 'iuKGfU0qJ1'
    }

    response = client.post("/api/customers", json=body)
    content = response.json()
    assert response.status_code == 422
    assert content['detail'][0]['msg'] == "Date format must be yyyy-MM-dd"

def test_customer_registration_with_birth_date_invalid(client: TestClient):
    body = {
	'name': 'Isaac',
	'last_name': 'Farias',
	'cpf': '98167244807',
	'birth_date': '1991-02-30',
	'email': 'isaac.farias@email.com',
	'password': 'iuKGfU0qJ1'
    }

    response = client.post("/api/customers", json=body)
    content = response.json()
    assert response.status_code == 422
    assert content['detail'][0]['msg'] == "day is out of range for month"

def test_customer_registration_with_cpf_not_numeric(client: TestClient):
    body = {
	'name': 'Isaac',
	'last_name': 'Farias',
	'cpf': 'numero__cpf',
	'birth_date': '1991-11-06',
	'email': 'isaac.farias@email.com',
	'password': 'iuKGfU0qJ1'
    }

    response = client.post("/api/customers", json=body)
    content = response.json()
    assert response.status_code == 422
    assert content['detail'][0]['msg'] == "Must be numeric"

def test_customer_registration_with_cpf_length_other_than_11(client: TestClient):
    body = {
	'name': 'Isaac',
	'last_name': 'Farias',
	'cpf': '1234567890',
	'birth_date': '1991-11-06',
	'email': 'isaac.farias@email.com',
	'password': 'iuKGfU0qJ1'
    }

    response = client.post("/api/customers", json=body)
    content = response.json()
    assert response.status_code == 422
    assert content['detail'][0]['msg'] == "Must be 11 characters long"

def test_customer_registration_with_cpf_in_use(client: TestClient):
    body = {
	'name': 'Isaac',
	'last_name': 'Farias',
	'cpf': '98167244806',
	'birth_date': '1991-11-06',
	'email': 'isaac2@email.com',
	'password': 'iuKGfU0qJ1'
    }

    response = client.post("/api/customers", json=body)
    content = response.json()
    assert response.status_code == 400
    assert content['message'] == "Usuário já cadastrado"

def test_customer_registration_with_email_in_use(client: TestClient):
    body = {
	'name': 'Isaac',
	'last_name': 'Farias',
	'cpf': '98167244807',
	'birth_date': '1991-11-06',
	'email': 'isaac@email.com',
	'password': 'iuKGfU0qJ1'
    }

    response = client.post("/api/customers", json=body)
    content = response.json()
    assert response.status_code == 400
    assert content['message'] == "Usuário já cadastrado"

def test_customer_registration_with_minor_age(client: TestClient):
    body = {
	'name': 'Luís',
	'last_name': 'Silveira',
	'cpf': '74491405433',
	'birth_date': '2005-11-06',
	'email': 'luis.silveira@email.com',
	'password': 'My3otkBDw8'
    }

    response = client.post("/api/customers", json=body)
    content = response.json()
    assert response.status_code == 422
    assert content['detail'][0]['msg'] == "You must be 18 or older to register"

def test_get_all_customers(client: TestClient):
    response = client.get("/api/customers")
    content = response.json()
    assert response.status_code == 200
    assert isinstance(content, list)

def test_get_customer_by_id(client: TestClient):
    response = client.get('/api/customers/6357da0cdd0f514fe3f943e5')
    assert response.status_code == 200
