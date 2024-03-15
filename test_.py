from playwright.sync_api import sync_playwright
import pytest
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

@pytest.mark.test
def test_add_contact(page):
    # Navigate to the website
    page.goto('https://thinking-tester-contact-list.herokuapp.com/')

    # Login
    page.fill('#email', 'phytontest@test.com')
    page.fill('#password', 'Testpass')
    page.click('#submit')

    # Generate random data for contact details
    first_name = generate_random_string(8)
    last_name = generate_random_string(10)
    email = generate_random_string(5) + '@example.com'

    # Click on the "Add Contact" button
    page.click('#add-contact')

    # Fill in the contact details
    page.fill('#firstName', first_name)
    page.fill('#lastName', last_name)
    page.fill('#email', email)

    # Click on the "Submit" button
    page.click('#submit')

    page.wait_for_timeout(1000)

    # Refresh the page
    page.reload()

    # Wait for the contact table to update
    page.wait_for_selector('.contactTableBodyRow')

    # Get the text content of the contact table
    contact_table_text = page.text_content('.contactTable')

    # Check if the contact table contains the generated data
    assert first_name in contact_table_text
    assert last_name in contact_table_text

# Use the 'headless' option set to False to run in non-headless mode
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    test_add_contact(page)  # Call the test function with the 'page' object
    context.close()
