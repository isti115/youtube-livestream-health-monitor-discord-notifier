import status
import message
import re

# import sched, time
# sch = sched.scheduler(time.time, time.sleep)

import time
import datetime

def update(comment, st):
    text = re.sub('"', '`', re.sub("'([^,]*?)':", '\\1:',
      '**' + comment + ':**\\n```js\\n' + str(st) + '\\n```'
    ))
    print(text)
    message.send_isti(text)

def loop():
    # starttime = time.time()
    # elif (time.time() - starttime) / 60 / 60 / 24 > 1:
    # st = status.get()
    st = None
    while True:
        new_st = status.get()
        now = datetime.datetime.now()
        if new_st != st:
            print('diff')
            st = new_st
            update("Friss helyzetjelentés", st)
        elif now.hour == 12 and now.minute <= 5:
            print('time')
            update("Déli helyzetjelentés", st)
        else:
            print('match')
        time.sleep(60 * 5)

if __name__ == "__main__":
    loop()
