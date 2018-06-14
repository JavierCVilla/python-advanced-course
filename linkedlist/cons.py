class Cons:
    def __init__(self, item, tail=None):
        self.item = item
        self.tail = tail


    def __getitem__(self, pos):
        if pos == 0:
            return self.item
        try:
            return self.tail[pos-1]
        except TypeError:
            raise IndexError

    def __len__(self):
        return sum(1 for item in self)

        # Alternative implementation
        #count = 1
        #while self.tail is not None:
	#    self = self.tail
	#    count += 1
	#return count

    # Alternative implementation of iterator
    # using a generator function
    def __iter__(self):
        cons = self
        while cons is not None:
            yield cons.item
            cons = cons.tail

    #def __iter__(self):
    #    return ConsIterator(self)


### Class not needed since we have implemented
### the iterator protocol using a generator function
### in the class itself
#class ConsIterator:
#    def __init__(self, cons):
#        self._cons = cons
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        if self._cons is None:
#            raise StopIteration
#        item = self._cons.item
#        self._cons = self._cons.tail
#        return item
#
#    next = __next__
###
