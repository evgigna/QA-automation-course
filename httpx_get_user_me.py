import httpx

login_data = {
    "email": "test@example.com",
    "password": "test"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",
                            json=login_data)

print(login_response.status_code)

login_response_data = login_response.json()
print(login_response_data)

user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=user_headers)
get_user_response_data = get_user_response.json()

print(get_user_response.status_code)
print(get_user_response_data)

