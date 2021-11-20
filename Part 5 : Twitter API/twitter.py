import json
import requests
from requests.api import head

## constants 
USER_ID = "1229189739863068673"
NAME = "frostByte"
SCREEN_NAME = "frostBy46228778"
BEARER = "AAAAAAAAAAAAAAAAAAAAAHkAWAEAAAAA9MvZGOmFtj2YW52VRTg29MmH3rE%3DsseSjy3gPVYyBqCGwUQdtPuImAvfi0kuGiSeF8FkL2mIBUyF2W"
REQ = f"https://api.twitter.com/1.1/users/show.json?user_id={USER_ID}"
HEADERS = {"authorization": f"Bearer {BEARER}"}

profile_info = requests.get(REQ,headers=HEADERS)
# from json object to python object
profile_info_deserialized = json.loads(profile_info.text) 
print(profile_info_deserialized['id'])
print(profile_info_deserialized["friends_count"])
print(profile_info_deserialized["followers_count"])