import json
import requests

discord = json.load(open('discord.json'))

def send(channel_id, content):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    data = '{"content":"%s"}' % content
    headers = {
        'Content-type': 'application/json',
        'Authorization': discord['authorization']
    }
    requests.post(url, data=data.encode('utf-8'), headers=headers)

def send_isti(content): send(discord['isti'], content)
def send_group(content): send(discord['group'], content)
