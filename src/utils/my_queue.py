from ..constant import *

class MyQueue():
    def __init__(self) -> None:
        self.__ = []

    def pop(self):
        if self.is_empty():
            return
        self.__.pop(0)

    def push(self, con):
        self.__.append(con)
    
    def get(self):
        if self.is_empty():
            return END
        return self.__[0]

    def size(self):
        return len(self.__)

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.__ = []
    
    def lazy_update(self, cons):
        self.__ = cons