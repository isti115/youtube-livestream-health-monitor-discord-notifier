import os
import os.path

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "secrets.json"

def get_credentials():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            creds = flow.run_console()
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

credentials = get_credentials()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

def get():
    request = youtube.liveStreams().list(
        part="snippet,status",
        mine=True
    )
    response = request.execute()

    continous = list(filter(
        lambda s: s['snippet']['title'] == 'Folyamatos',
        response['items']
    ))[0]

    return continous['status']
