import requests

def test_add_and_retrieve_contact():
    # Login data
    login_data = {
        "email": "phytontest@test.com",
        "password": "Testpass"
    }

    # Log in to obtain the authentication token
    login_response = requests.post(
        'https://thinking-tester-contact-list.herokuapp.com/users/login',
        headers={'Content-Type': 'application/json'},
        json=login_data
    )

    assert login_response.status_code == 200
    assert login_response.ok

    # Extract the token from the login response
    response_body = login_response.json()
    token = response_body['token']

    assert token

    # Contact data to be added
    contact_data = {
        "firstName": "George",
        "lastName": "Test",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }

    # Add a new contact using the authentication token
    add_contact_response = requests.post(
        'https://thinking-tester-contact-list.herokuapp.com/contacts',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        },
        json=contact_data
    )

    assert add_contact_response.status_code == 201
    assert add_contact_response.ok

    # Retrieve contacts using the authentication token
    get_contacts_response = requests.get(
        'https://thinking-tester-contact-list.herokuapp.com/contacts',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert get_contacts_response.status_code == 200
    assert get_contacts_response.ok

    # Extract the contacts from the response
    contacts = get_contacts_response.json()

    # Verify that the added contact is present in the response
    added_contact = next((contact for contact in contacts if contact['firstName'] == "George" and contact['lastName'] == "Test"), None)
    assert added_contact

test_add_and_retrieve_contact()
