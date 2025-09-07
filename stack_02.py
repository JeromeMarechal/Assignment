class MyQueue(object):

    def __init__(self):
        self.sck_in = []
        self.sck_out = []

        

    def push(self, x: int) -> None:
        self.sck_in.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.sck_out.pop()
        

    def peek(self) -> int:
        if not self.sck_out:
            while self.sck_in:
                self.sck_out.append(self.sck_in.pop())
            return self.sck_out[-1]    
        

    def empty(self) -> bool:
        return not self.sck_in and not self.sck_out