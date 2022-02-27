# Dependencies:
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- requests

# Setup
0. Install the dependencies  
   (I would recommend using [`pipenv`](https://github.com/pypa/pipenv))
1. Create a project through the Google Developer Console  
   (https://console.developers.google.com/home/dashboard?project=zal1000&pli=1)
2. Download the corresponding secrets and place them into `google_secrets.json`  
   (https://developers.google.com/youtube/registering_an_application)
3. Create a Discord account and obtain its authorization key and place it into
   the _authorization_ field of `settings.json` (Check network requests from
   your browser's DevTools or use some other similar method.)
4. Create a Discord group DM where notifications should be sent and place its
   ID into the _channel_id_ field of `settings.json`
5. Obtain the name of the stream key from YouTube that you'd like to monitor
   and write it into the _stream_key_name_ field of `settings.json`

# Usage
Start the application in a terminal by running `python main.py`!  
(In case Python 2 is your default version you need to specify `python3 main.py`)

_Note:_ On the first execution it will guide you through an authorization
process, where you need to paste a url from the command line into a browser and
obtain a token, which is then pasted back into the shell.
