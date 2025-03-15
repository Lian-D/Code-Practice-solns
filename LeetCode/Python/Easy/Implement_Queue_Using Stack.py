class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x):
        self.s1.append(x)

    def pop(self):
        while (self.s1):
            self.s2.append(self.s1.pop())
        ret = self.s2.pop()
        while (self.s2):
            self.s1.append(self.s2.pop())
        return ret

    def peek(self):
        while (self.s1):
            self.s2.append(self.s1.pop())
        ret = self.s2.pop()
        self.s1.append(ret)
        while (self.s2):
            self.s1.append(self.s2.pop())
        return ret

    def empty(self):
        return max (len(self.s1), len(self.s2)) == 00
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()