
class MyList:

    def __init__(self):
        self.size = 0
        self.data = []

    def add(self, value):
        self.data.append(value)
        self.size += 1

    def clear(self):
        self.size = 0
        self.data = []

    def remove(self, pos):
        if pos > self.size or pos < 0:
            raise IndexError("{pos} position not valid")
        del self.data[pos]
        self.size -= 1

    def get(self, pos):
        if pos > self.size or pos < 0:
            raise IndexError("{pos} position not valid")
        return self.data[pos]

    def contains(self, value):
        for val in self.data:
            if val == value:
                return True
        return False

    def get_size(self):
        return self.size

    def search(self, val):
        for i in range(self.size):
            if self.data[i] == val:
                return i
        return -1
