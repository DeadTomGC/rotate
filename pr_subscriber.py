from Queue import *
from threading import *

import zmq
from pr_message import *

class pr_subscriber(Thread):
    def __init__(self, top = None, loc = "tcp://localhost:5556"):
        Thread.__init__(self)
        self.loc = loc
        self.top = top
        self.messages = Queue()
        self.listen = True
    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(self.loc)
        if self.top:
            socket.setsockopt(zmq.SUBSCRIBE, self.top)
        while self.listen:
            string = socket.recv()
            self.messages.put(string)
    def poll(self):
        res = None
        try:
            res = self.messages.get_nowait()
        except Empty:
            return res
        return pr_message.decode(res)
    def kill(self):
        self.listen = False
