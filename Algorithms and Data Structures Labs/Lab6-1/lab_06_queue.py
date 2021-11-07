import myDataStructures as da
import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--inputFileName")
args = parser.parse_args()
"""
class ArrayQueue:
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

def read_file(inputFileName, queue):
	queue = da.Queue()
	read_file = open(inputFileName, 'r').readlines()
	for i in read_file:
		queue._enqueue(i)
	return queue

def palindrome(Array_Queue):
	Queue = da.Queue()
	reverse_queue = da.Queue()
	initial_list = []
	queue_list = []
	if Array_Queue != None:
		dequeue = Array_Queue._dequeue()
		initial_list.append(dequeue)
		Queue._enqueue(dequeue)
	queue_list = initial_list[::-1]
	for i in queue_list:
		Array_Queue._enqueue(i)
		Queue._enqueue(i)
	if Queue == reverse_queue:
		return True
	else:
		return False
def reverse(Array_queue):
	our_list = da.Queue()
	the_list = []
	if not Array_queue.isempty():
		dequeue = Array_queue._dequeue() 
		the_list.append(dequeue)
	new_list = the_list[::-1]
	our_list._enqueue(new_list)
	return our_list

def length_and_sum(array_Queue):
	sum_of_nums = 0
	count = 0
	our_list = []
	while not array_Queue.isempty():
		dequeue = array_Queue._dequeue()
		our_list.append(dequeue)
	for i in our_list:
		integer = int(i)
		count = len(our_list)
		sum_of_nums += integer
	return (count, sum_of_nums)

def main():
	our_queue = da.Queue()
	populate_obj = read_file(args.inputFileName, our_queue)
	our_queue_list = da.Queue()
	for i in range(len(our_queue)):
		dequeue = our_queue[i]._dequeue()
		our_queue_list._enqueue(dequeue)

	#copy_queue = copy.deepcopy(our_queue)
	palindrome_yes = palindrome(populate_obj)
	print(palindrome_yes)
	reverse_queue = reverse(our_queue_list)
	palindrome_yes_yes = palindrome(reverse_queue)
	print(palindrome_yes_yes)
	print(populate_obj._front())
	print(length_and_sum(populate_obj))

if __name__ == '__main__':
	main()
