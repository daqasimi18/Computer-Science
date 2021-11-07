import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFileName")
args = parser.parse_args()

class node:
	def __init__(self, domain=None):
		self.domain = domain
		self.count = 0
		self.next = None

	def get_domain(self):
		return self.domain

class single_linked_list:
	def __init__(self):
		self.head = node()
		self.tail = None
		
	def linked_list_style(self, domain):
		new_node = node(domain)
		current = self.head
		while current.next != None:
			current = current.next
			self.tail.next = None
			self.count += 1
		current.next = new_node

	def unique_linked_list(self, domains):
		current = domains.head
		unique_list = []
		while current.next != None:
			if current.get_domain() not in unique_list:
				unique_list.append(current.get_domain())
			current = current.next
		return len(unique_list)-1

	def append(self, domain):
		new_node = node(domain)
		current = self.head
		while current.next != None:
			current = current.next
		current.next = new_node

	def length(self):
		current = self.head
		count = 0
		while current.next != None:
			count += 1
			current = current.next
		return count

def read_file(inputFileName):
	read_file = open(inputFileName, 'r').readlines()
	our_list = []
	item = dict()
	for i in read_file:
		split = i.split(":")
		domain = split[0]
		our_list.append(domain)
	for j in our_list:
		if j in item:
			item[j] += 1
		else:
			item[j] = 1
	item = {key:value for key, value in item.items() if value>1}
	for key, value in item.items():
		print(key, ':', value)

def popular(our_list):
	domain = our_list[0]
	count = 0
	for i in our_list:
		current_frequency = our_list.count(i)
		if current_frequency > count:
			count = current_frequency
			domain = i
	return domain, count

def popular_percentage(our_list):
	domain = our_list[0]
	count = 0
	for i in our_list:
		current_frequency = our_list.count(i)
		if current_frequency > count:
			count = current_frequency
			domain = i
	return (float(count)/float(len(our_list)))*100

def main():
	my_file = single_linked_list()
	our_list = read_file(args.inputFileName)
	unique_list = []
	for i in our_list:
		my_file.append(i)
	print(my_file.length())
	print(my_file.unique_linked_list(my_file))
	print(popular(our_list))
	print(popular_percentage(our_list))

if __name__=="__main__":
	main()



