from requests.auth import HTTPDigestAuth
import requests
import sys
import json

#variable input for username and group id
in_username = "userNametoRemove"
in_group_id =  "yourGroupID_Atlas"
temp_list = []
final_list = " "

base_url = "https://cloud.mongodb.com/api/atlas/v1.0"
pub_key = "yourPublicKeyAtlas"
priv_key = "yourPrivateKeyAtlas"
headers_post = {"Accept": "application/json",
                "Content-Type": "application/json"
                }

#get user scope (environment) for output purpose
req_get = requests.get(f"{base_url}/groups/{in_group_id}/databaseUsers/admin/{in_username}",auth=HTTPDigestAuth(pub_key,priv_key), headers=headers_post)
if req_get.status_code == 200:
    req_get_parsed = json.loads(req_get.content)
    for scope in req_get_parsed['scopes']:
        temp_list.append(scope['name'])
    print("Success to retrieve data from MongoDB Atlas")
else:
    print(f"Failed to retrieve data from MongoDB Atlas response code: {req_get.status_code}")
    sys.exit(1)

#delete user
req_delete = requests.delete(f"{base_url}/groups/{in_group_id}/databaseUsers/admin/{in_username}",auth=HTTPDigestAuth(pub_key,priv_key))
if req_delete.status_code == 204:
    print(f"{in_username} user have been revoked from mongodb and its DB environment access was {final_list.join(temp_list)}")
else:
    print(f"Failed to delete user from MongoDB Atlas response code: {req_delete.status_code}")