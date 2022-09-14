from requests.auth import HTTPDigestAuth
import requests
import json
import sys

#variable input for username, group id and environment choices
in_group_id =  "yourGroupID_Atlas"
list_sorter = []
base_url = "https://cloud.mongodb.com/api/atlas/v1.0"
pub_key = "yourPublicKeyAtlas"
priv_key = "yourPrivateKeyAtlas"
auth_key = {f'{pub_key}': f'{priv_key}'}
headers_post = {"Accept": "application/json",
                "Content-Type": "application/json"
                }

req = requests.get(f"{base_url}/groups/{in_group_id}/databaseUsers",auth=HTTPDigestAuth(pub_key,priv_key), headers=headers_post)
if req.status_code == 200:
    req_parsed = json.loads(req.content)
    for mongo_user in req_parsed['results']:
        list_sorter.append(mongo_user['username'])
        list_sorter.sort()

    for user in list_sorter:
        print(user)
else:
    print("Failed to retrieve data from MongoDB Atlas")
    sys.exit(1)
    