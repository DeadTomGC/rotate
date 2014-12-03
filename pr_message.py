import pickle
from time import *

class pr_message:
    def __init__(self, data, top = "default", tstamp = None):
        self.data = data
        self.top = top
        self.tstamp = tstamp
    def stamp(self):
        tstamp = time()
        ret = 0
        if self.tstamp:
            ret = tstamp - self.tstamp
        self.tstamp = tstamp
        return ret
    def delta(self):
        ret = 0
        if self.tstamp:
            ret = time() - self.tstamp
        return ret
    def encode(self):
        self.stamp()
        return self.top + " " + str(self.tstamp) + " " + pickle.dumps(self.data)
    @staticmethod
    def decode(msg):
        t, s, d = msg.split(' ', 2)
        return pr_message(pickle.loads(d), t, float(s))
