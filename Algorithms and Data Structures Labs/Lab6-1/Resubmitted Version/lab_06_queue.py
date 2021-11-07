import myDataStructures as da
import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--inputFileName")
args = parser.parse_args()

def read_file(inputFileName, queue):
	queue = da.Queue()
	read_file = open(inputFileName, 'r').readlines()
	for i in read_file:
		queue.enqueue(i)
	return queue

def palindrome(Array_Queue):
	Queue = da.Queue()
	reverse_queue = da.Queue()
	initial_list = []
	queue_list = []
	if Array_Queue != None:
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
	our_list = da.Queue()
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
	our_queue = da.Queue()
	populate_obj = read_file(args.inputFileName, our_queue)
	#first_que_copy = da.Queue()
	#second_que_copy = da.Queue()
	#for i in range(len(our_queue)):
		#dequeue = our_queue[i]
		#first_que_copy.enqueue(dequeue)
		#second_que_copy.enqueue(dequeue)
	palindrome_yes = palindrome(populate_obj)
	print(palindrome_yes)
	reverse_queue = reverse(our_queue)
	palindrome_yes_yes = palindrome(reverse_queue)
	print(palindrome_yes_yes)
	print(populate_obj.front())
	print(length_and_sum(populate_obj))

if __name__ == '__main__':
	main()
