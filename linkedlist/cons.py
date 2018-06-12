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
	if self.tail is None:
            return 1
        return len(self.tail) + 1

        # Alternative implementation
        #count = 1
        #while self.tail is not None:
	#    self = self.tail
	#    count += 1
	#return count
