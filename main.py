import status
import message
import re

import time
import datetime

def update(comment, st):
    text = re.sub('"', '`', re.sub("'([^,]*?)':", '\\1:',
      '**' + comment + ':**\\n```js\\n' + str(st) + '\\n```'
    ))
    print(text)
    message.send_isti(text)

def loop():
    # st = status.get()
    st = None
    while True:
        print(f'check at: {datetime.datetime.now().isoformat()}')
        new_st = status.get()
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
