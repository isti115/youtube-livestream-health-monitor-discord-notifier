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
    no_data_first = True
    while True:
        now = datetime.datetime.now()
        print(f'check at: {now.isoformat()}')
        new_st = status.get(settings['stream_key_name'])
        if new_st != st:
            print('diff')
            if new_st['healthStatus']['status'] == 'noData' and no_data_first:
                print('noData -> retry set')
                no_data_first = False
                time.sleep(60 * 1)
            else:
                st = new_st
                no_data_first = True
                update('Health change notice', st)
                time.sleep(60 * 5)
        elif now.hour == 12 and now.minute < 5:
            print('time')
            update('Midday status report', st)
            time.sleep(60 * 5)
        else:
            print('match')
            time.sleep(60 * 5)

if __name__ == "__main__":
    loop()
