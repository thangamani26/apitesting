import requests

# Example for POST request with custom headers
request_headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 0b5b0eac4854cb5fdd8048c8406cb60fc8476e30dee6d2fb8a64a7ad7e86749e'
}

request_body = {
    "name": "Rep. Tejas Kaniyar",
    "email": "userabc112123@legros.example",
    "gender": "male",
    "status": "inactive"
}

response = requests.post('https://gorest.co.in/public/v2/users',
                         headers=request_headers, json=request_body)

print(response.status_code)
print(response.json())
print(response.headers)

assert response.status_code == 201
