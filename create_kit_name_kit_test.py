import data
import sender_stand_request
import json

# Parametros Globales
NEW_USER_DATA = data.user_data.copy()
new_user_token = sender_stand_request.get_new_user_token(NEW_USER_DATA)
print(new_user_token)
variable_queRecibeElValorReturn = sender_stand_request.post_new_client_kit(new_user_token, { "name": "a"})
print(variable_queRecibeElValorReturn)

def possitive_assert_status_code(code):
    assert code == 201

def possiive_assert_created_kit_name(kit_name_requested, kit_name_created):
    assert kit_name_requested == kit_name_created

def negative_assert_status_code(code):
    assert code == 400

def test_create_kit_single_character():
    kit_name = 'a'
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    dict_body_response = json.loads(response.text)
    created_kit_name = dict_body_response['name']
    possitive_assert_status_code(response.status_code)
    possiive_assert_created_kit_name(kit_name, created_kit_name)

def test_create_kit_511_characters():
    kit_name = 'a'*511
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    dict_body_response = json.loads(response.text)
    created_kit_name = dict_body_response['name']
    possitive_assert_status_code(response.status_code)
    possiive_assert_created_kit_name(kit_name, created_kit_name)

def test_create_kit_0_characters():
    kit_name = ''
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    negative_assert_status_code(response.status_code)

def test_create_kit_512_characters():
    kit_name = 'a'*512
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    negative_assert_status_code(response.status_code)

def test_create_kit_special_characters():
    kit_name = '"№%@","'
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    dict_body_response = json.loads(response.text)
    created_kit_name = dict_body_response['name']
    possitive_assert_status_code(response.status_code)
    possiive_assert_created_kit_name(kit_name, created_kit_name)

def test_create_kit_space_characters():
    kit_name = " A Aaa "
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    dict_body_response = json.loads(response.text)
    created_kit_name = dict_body_response['name']
    possitive_assert_status_code(response.status_code)
    possiive_assert_created_kit_name(kit_name, created_kit_name)

def test_create_kit_numeric_characters():
    kit_name = "123"
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    dict_body_response = json.loads(response.text)
    created_kit_name = dict_body_response['name']
    possitive_assert_status_code(response.status_code)
    possiive_assert_created_kit_name(kit_name, created_kit_name)

def test_create_kit_empty_body():
    kit_body = {}
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    negative_assert_status_code(response.status_code)

def test_create_kit_integer_type_name():
    kit_name = 123
    kit_body = {
        "name": kit_name
    }
    response = sender_stand_request.post_new_client_kit(new_user_token, kit_body)
    negative_assert_status_code(response.status_code)