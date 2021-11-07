import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFileName")
args = parser.parse_args()

class item:
	def __init__(self, name, priority):
		self.name = name
		self.priority = priority
		self.next = None

	def get_name(self):
		return self.name
	def set_name(self, new_name):
		self.name = new_name

	def get_priority(self):
		return self.priority
	def set_priority(self, new_priority):
		self.priority = new_priority

	def get_next(self):
		return self.next
	def set_next(self, new_next):
		self.next = new_next

class PriorityQueue:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_item(self, names, priorities):
		current_item = item(names, priorities)
		if self.head == None:
			self.head = current_item
			self.tail = current_item
		elif priorities > self.head.priority:
			current_item.set_next(self.head)
			self.head = current_item
		else:
			current = self.head
			while current.next and current.next.priority > priorities:
				current = current.next
			current_item.set_next(current.next)
			current.set_next(current_item)
			if self.tail == current:
				self.tail = current_item

	def remove(self):
		current = self.head
		self.head = self.head.next
		current.next = None

def read_file(inputFileName):
	read_file = open(inputFileName, 'r').readlines()
	our_list = PriorityQueue()
	for i in read_file:
		split = i.split(',')
		names = split[0]
		priorities = int(split[1].strip())
		our_list.insert_item(names, priorities)
	return our_list
		
def main():
	our_list = read_file(args.inputFileName)
	print(our_list.head.name)
	our_list.remove()
	print(our_list.head.name)
	print(our_list.tail.name)

if __name__=="__main__":
	main()
