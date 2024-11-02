from collection import Collection
from listiterator import ListIterator
class ListColleciton(Collection):
    def __init__(self):
        self.items=[]
    def add__item(self, item):
        self.items.append(item)
    def create_iterator(self):
        return ListIterator(self.items)