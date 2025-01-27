import sender_stand_request
import data
from data import user_body

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_1_letter_in_the_name_success_response():
    current_kit_body = get_kit_body("a")
    positive_assert(current_kit_body)

def test_511_letter_in_the_name_success_response():
    current_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(current_kit_body)

def test_no_letters_in_the_name_no_success_response():
    current_kit_body = get_kit_body("")
    negative_assert_400(current_kit_body)

def test_512_letters_in_the_name_no_success_response():
    current_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_400(current_kit_body)

def test_special_characters_in_the_name_success_response():
    current_kit_body = get_kit_body("№%@")
    positive_assert(current_kit_body)

def test_with_spaces_in_the_name_success_response():
    current_kit_body = get_kit_body("A Aaa")
    positive_assert(current_kit_body)

def test_with_numbers_in_the_name_success_response():
    current_kit_body = get_kit_body("123")
    positive_assert(current_kit_body)

def test_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

def test_without_string_numbers_in_the_name_no_success_response():
    current_kit_body = get_kit_body(123)
    negative_assert_400(current_kit_body)













