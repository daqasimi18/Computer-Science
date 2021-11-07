import darabaliqasimi_lab5 as da
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
class Queue:
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
def main():
	stack = Stack()
	queue = Queue()
	stack._push(5)
	stack._push(10)
	stack._push(10)
	queue._enqueue(11)
	queue._enqueue(12)
	queue._enqueue(13)
	print(queue._front())
	print(stack._top())


if __name__ == "__main__":
	main()

