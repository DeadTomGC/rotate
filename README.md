This is a simple demo using pyro that relies on the irobotcreate

The primary files to edit here are rotate.py, KinectMonitor.py and IPC.py

In IPC, you can change the update rate.

rotate.py is teh subscriber and simply attempts to face the user given to it by the publisher.

KinectMonitor is the publisher.  It's job is to figure out where the user is.  This is somewhat difficult since false positive pop up from time to time and the user's skeleton gets dropped pretty frequently too. 

