import json
import requests
from requests.api import head

## constants 
USER_ID = "1229189739863068673"
NAME = "frostByte"
SCREEN_NAME = "elonmusk"
BEARER = "AAAAAAAAAAAAAAAAAAAAAHkAWAEAAAAAeY2cd581sWENnwbXtkzjYBGCXOg%3DlrQuD2lQrRqhKviSlNRcntSJursTmn0XJ3gjvWbiMbppgUumP5"
REQ = f"https://api.twitter.com/1.1/users/show.json?screen_name={SCREEN_NAME}"
HEADERS = {"authorization": f"Bearer {BEARER}"}

profile_info = requests.get(REQ,headers=HEADERS)
# from json object to python object
profile_info_deserialized = json.loads(profile_info.text) 
print(profile_info_deserialized['id'])
print(profile_info_deserialized["friends_count"])
print(profile_info_deserialized["followers_count"])

REQ2 = f'https://api.twitter.com/1.1/friends/list.json?screen_name={SCREEN_NAME}'

profile_info = requests.get(REQ2,headers=HEADERS)
# from json object to python object
friends_deserialized = json.loads(profile_info.text) 
for users in friends_deserialized['users']:
    print(users['screen_name'])
