class Counter:
    def __init__(self):
        self.counter = 0

    def getID(self):
        self.counter = self.counter + 1
        return self.counter
