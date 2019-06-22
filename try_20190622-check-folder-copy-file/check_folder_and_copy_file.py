from distutils.dir_util import copy_tree
import sched, time

s = sched.scheduler(time.time, time.sleep)

def copy2folder(sc):

    root = "C:\\Users\\dir"
    destination = "C:\\Users\\dir2"
    copy_tree(root, destination)

    s.enter(5, 1, copy2folder, (sc,))

s.enter(5, 1, copy2folder, (s,))
s.run()



