import json
import requests
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
# REFRESH_ENDPOINTS= AUTH_ENDPOINTS+'refresh/'
ENDPOINTS='http://127.0.0.1:8000/api/v1/list'
headers={
    "Content-Type":"application/json"
}
data={
    'username':'andy',
    'password':'1234'
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data),         headers=headers)
token=r.json()
print(token)
# refresh_data={
#     'token':token
# }
#
# new_response=requests.post(REFRESH_ENDPOINTS,data=json.dumps(refresh_data),headers=headers)
# new_token = new_response.json()
#
# print(new_token)
# headers={
#     "Content-Type":"application/json",
#     "Authorization":"JWT"+token,
# }
# post_data=json.dumps({'content':'some reamdijkbndiojkn'})
# posted_response=requests.post(ENDPOINTS,data=post_data,headers=headers)
# print(posted_response.text)