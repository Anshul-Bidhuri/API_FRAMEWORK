###########################LOGIN_PAGE################################################

login_base_url = 'https://reqres.in/api/login'

correct_login_credentials = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

incorrect_login_credentials = {
    "email": "fqeff",
    "password": "cityslicka"
}

###########################USER_PAGE################################################

user_page_get_list_user_url = "https://reqres.in/api/users?page={}"
user_page_create_user_url = "https://reqres.in/api/users"

user_details_empty_job_field = {
    "name": "morpheus",
    "job": ""
}
