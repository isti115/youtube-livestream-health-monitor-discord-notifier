import requests

def send(authorization, channel_id, content):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    data = '{"content":"%s"}' % content
    headers = {
        'Content-type': 'application/json',
        'Authorization': authorization
    }
    requests.post(url, data=data.encode('utf-8'), headers=headers)
    print('Sent:', content)
