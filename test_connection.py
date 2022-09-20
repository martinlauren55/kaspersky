import requests
import base64
import urllib3
import json

from config import LOGIN, PASSWORD, BASE_URL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user64 = base64.b64encode(LOGIN.encode('utf-8')).decode("utf-8")
password64 = base64.b64encode(PASSWORD.encode('utf-8')).decode("utf-8")
auth_headers = {'Authorization': 'KSCBasic user="' + user64 + '", pass="' + password64 + '"',
                'Content-Type': 'application/json', }

tokenurl = BASE_URL + 'Session.StartSession'
tokenbody = {}
tokenrequest = requests.post(tokenurl, headers=auth_headers, data=tokenbody, verify=False)

print(f'status_code: {tokenrequest.status_code}')

token = tokenrequest.json().get('PxgRetVal')
print(f'token: {token}')
