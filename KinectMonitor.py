from IPC import *
from nitepy import *
from pr_publisher import *
from pr_message import *
import numpy as np
import sys





track = lib.Tracker_new()
pub = pr_publisher("Goal", "tcp://*:5556")

InitSync()
oldx = -2000
while True:
    x = 0
    z = 1
    lib.loop(track)
    i=0
    while i<lib.getUsersCount(track):
        if lib.getUserCOMX(track,i)>-1500 and lib.getUserCOMX(track,i)<1500 and lib.getUserCOMZ(track,i)>400 and (np.abs(lib.getUserCOMX(track,i)-oldx)<500 or oldx<-1500):
            x = lib.getUserCOMX(track,i)
            oldx = x
            z = lib.getUserCOMZ(track,i)
            break
        i=i+1
    msg = pr_message([x,z], "Goal")
    print msg.data
    pub.send(msg)

        
    Sync()
