import json
import requests

discord = json.load(open('discord.json'))

def send(url, content):
    data = '{"content":"' + content + '"}'
    headers = {
        'Content-type': 'application/json',
        'Authorization': discord['authorization']
    }
    r = requests.post(url, data=data.encode('utf-8'), headers=headers)

def send_isti(content): send(discord['isti'], content)
def send_group(content): send(discord['group'], content)
