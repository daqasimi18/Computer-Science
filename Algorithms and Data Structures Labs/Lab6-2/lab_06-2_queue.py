import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--inputFileName")
args = parser.parse_args()

class ArrayQueue:
    def __init__(self):
        self._queue=[]
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

def read_file(inputFileName, Queue):
	Queue = ArrayQueue()
	read_file = open(inputFileName, 'r').readlines()
	for i in read_file:
		Queue.enqueue(i)
	return Queue

def palindrome(Array_Queue):
	Queue = ArrayQueue()
	reverse_queue = ArrayQueue()
	initial_list = []
	queue_list = []
	if not Array_Queue.isempty():
		dequeue = Array_Queue.dequeue()
		initial_list.append(dequeue)
		Queue.enqueue(dequeue)
	queue_list = initial_list[::-1]
	for i in queue_list:
		Array_Queue.enqueue(i)
		Queue.enqueue(i)
	if Queue == reverse_queue:
		return True
	else:
		return False
def reverse(Array_queue):
	our_list = ArrayQueue()
	the_list = []
	if not Array_queue.isempty():
		dequeue = Array_queue.dequeue() 
		the_list.append(dequeue)
	new_list = the_list[::-1]
	our_list.enqueue(new_list)
	return our_list

def length_and_sum(array_Queue):
	sum_of_nums = 0
	count = 0
	our_list = []
	while not array_Queue.isempty():
		dequeue = array_Queue.dequeue()
		our_list.append(dequeue)
	for i in our_list:
		integer = int(i)
		count = len(our_list)
		sum_of_nums += integer
	return (count, sum_of_nums)

def main():
	our_queue = ArrayQueue()
	populate_obj = read_file(args.inputFileName, our_queue)
	copy_queue = copy.deepcopy(our_queue)
	palindrome_yes = palindrome(populate_obj)
	print(palindrome_yes)
	reverse_queue = reverse(our_queue)
	palindrome_yes_yes = palindrome(reverse_queue)
	print(palindrome_yes_yes)
	print(populate_obj.front())
	print(length_and_sum(populate_obj))

if __name__ == '__main__':
	main()
