from iterator import Iterator
class ListIterator(Iterator):
    def __init__(self, collection):
        self.collection=collection
        self.pos=0
    def has_next(self):
        return self.pos<len(self.collection)-1
    def next(self):
        if self.has_next():
            self.pos+=1
            return self.collection[self.pos]
        else:
            raise "LimitError"
    
