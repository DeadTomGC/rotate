from pr_subscriber import *
from pr_message import *
import numpy as np
from IPC import *

#Utilities
from iRobotCreate import *
r = iRobotCreate(0, 20, "COM3")
time.sleep(1)

sub = pr_subscriber("Goal", "tcp://localhost:5556")
InitSync()
sub.start()
while True:
    msg = sub.poll() 
    while msg == None:
        msg = sub.poll()
    if np.abs(msg.data[0])>100:
        r.setvel(0,msg.data[0]/1000)
    else:
        r.setvel(0,0)
    print msg.data,np.arctan2(msg.data[0],msg.data[1])
    Sync()