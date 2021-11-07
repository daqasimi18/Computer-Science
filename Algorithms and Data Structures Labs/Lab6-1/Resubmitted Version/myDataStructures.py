import darabaliqasimi_lab5 as da
class Stack:
    def __init__(self):
        self._stack= da.DynamicArray()
        self._n=0

    def isempty(self):
        return self._n==0

    def size(self):
        return len(self._n)

    def push(self, a):
        self._stack.append(a)
        self._n+=1

    def top(self):
        top=self._stack[self._n-1]
        return top

    def pop(self):
        if self.isempty( ):
            raise ValueError( "Stack is empty" )
        pop_1=self._stack[self._n-1]
        self._n-=1
        return pop_1
    def front(self):
    	return self._stack[self._n-1]
"""
class Stack:
	def __init__(self):
		self.stack_list = da.DynamicArray()
		self._n = 0
	def _push(self, item):
		if item != None:
			self.stack_list.insertEfficient(self._n, item)
			self._n += 1
	def _pop(self): 
		first_item = delete(self.stack_list[0])
		return first_item
	def _top(self):
		return self.stack_list[0]
"""
class Queue:
	def __init__(self):
		self._queue= da.DynamicArray()
		self._n = 0
	def isempty(self):
		return self._n == 0
	def enqueue(self, a):
		self._n+=1
		return self._queue.append(a)
	def print_queue(self):
		for i in range(self._queue.__len__()):
			print(self._queue.__getitem__(i))
	def front(self):
		top=self._queue[self._n-1]
		return top
	def dequeue(self):
		if self.isempty():
			raise ValueError( "Stack is empty" )
		dequeue_1=self._queue[self._n-1]
		self._n-=1
		return dequeue_1
	def front(self):
		return self._queue[self._n-1]



	"""
	def __init__(self):
		self.items = da.DynamicArray()
	def __len__(self):
		return len(self.items)
	def _enqueue(self, item):
		self.items.insert(0, item)
	def _dequeue(self, item):
		remove_item = self.items[:-1]
		for j in self.items:
			self.items.delete(remove_item)
	def _front(self):
		return self.items[0]
	def _print(self):
		for i in self.items:
			print(i)
	"""
def main():
	stack = Stack()
	queue = Queue()
	"""
	stack._push(5)
	stack._push(10)
	stack._push(10)
	queue.enqueue(11)
	queue.enqueue(12)
	queue.enqueue(13)
	print(queue.front())
	print(stack._top())
	"""


if __name__ == "__main__":
	main()

