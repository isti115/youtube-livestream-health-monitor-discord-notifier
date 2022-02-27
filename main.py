import status
import discord

import json
import time
import datetime
import re

settings = json.load(open('settings.json'))

def make_code_block(state):
    return (
        re.sub('"', '`',
        re.sub("'([^,]*?)':", '\\1:',
            f'```js\\n{state}\\n```'
        ))
    )

def update(comment, st):
    text = f'**{comment}:**\\n{make_code_block(st)}'
    discord.send(settings['authorization'], settings['channel_id'], text)

def loop():
    # st = status.get()
    st = None
    while True:
        print(f'check at: {datetime.datetime.now().isoformat()}')
        new_st = status.get(settings['stream_key_name'])
        now = datetime.datetime.now()
        if new_st != st:
            print('diff')
            st = new_st
            update('Health change notice', st)
        elif now.hour == 12 and now.minute < 5:
            print('time')
            update('Midday status report', st)
        else:
            print('match')
        time.sleep(60 * 5)

if __name__ == "__main__":
    loop()
