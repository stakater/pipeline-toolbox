import json
import requests
from requests.auth import HTTPBasicAuth

def send_api_request(url, username, password):
   try:
       response = requests.get(url, auth=HTTPBasicAuth(username, password))
       if response.status_code == 200:
           parsed_data = json.loads(response.text)
           return parsed_data
       else:
           print(f"Request failed with status code: {response.status_code}")
           print(f"Response content: {response.text}")
           return None
   except requests.exceptions.RequestException as e:
     print(f"Error occurred during the API request: {e}")
     return None

def fetch_params(provider, username, password, hash, workspace, repository):

    if provider == "bitbucket-cloud":

      url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repository}/pullrequests"

      response = send_api_request(url, username, password)
      found = False
      for pull_request in response['values']:
        if found == True:
          break
        pull_request_id = pull_request['id']
        url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repository}/pullrequests/{pull_request_id}/commits"
        commits = send_api_request(url, username, password)

        if commits:
          for commit in commits['values']:
            print(f"Commit ID: {commit['hash']}, Author: {commit['author']['raw']}, Message: {commit['message']}")
            if commit['hash'] == hash:
              print(f"Found hash in PR {pull_request_id}")
              found = True
              break