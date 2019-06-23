import shutil
import os
import sched, time

s = sched.scheduler(time.time, time.sleep)

def move2folder(sc):

    source = 'C:\\path'
    dest1 = 'C:\\path2'

    files = os.listdir(source)

    for f in files:
            shutil.move(source+f, dest1)

    s.enter(5, 1, move2folder, (sc,))

s.enter(5, 1, move2folder, (s,))
s.run()

