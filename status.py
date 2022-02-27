import os
import os.path

from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
# import googleapiclient.errors

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "google_secrets.json"

def get_credentials():
    creds = None

    if os.path.exists('google_token.json'):
        creds = Credentials.from_authorized_user_file('google_token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes
            )
            creds = flow.run_console()
        with open('google_token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

credentials = get_credentials()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials
)

def get(stream_key_name):
    request = youtube.liveStreams().list(
        part="snippet,status",
        mine=True
    )
    response = request.execute()

    selected = list(filter(
        lambda s: s['snippet']['title'] == stream_key_name,
        response['items']
    ))[0]

    return selected['status']
