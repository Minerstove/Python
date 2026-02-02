class Stage():
    def __init__(self):
        self.left = []
        self.right = []

    def insert_left(self, s):
        self.left.append(s)
    
    def insert_right(self, s):
        self.right.append(s)

    def get(self, i):
        if 0 <= i < (len(self.left) + len(self.right)):
            if i < len(self.left):
                return self.left[-1 - i]
            else:
                return self.right[i - len(self.left)]
        else:
            raise ValueError("Not in range")