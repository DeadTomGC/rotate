import zmq

class pr_publisher:
    def __init__(self, top = "default", loc = "tcp://*:5556"):
        self.loc = loc
        self.top = top
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.bind(self.loc)
    def send(self, msg):
        if not self.top == msg.top:
            print "Error: topic mismatch."
        else:
            self.socket.send(msg.encode())
