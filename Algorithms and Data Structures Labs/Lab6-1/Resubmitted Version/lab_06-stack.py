import myDataStructures as da
import argparse
import copy

parser = argparse.ArgumentParser()
parser.add_argument("-i","--inputFileName")
args = parser.parse_args()

def read_file(inputFileName, stack):
	stack = da.Stack()
	read_file = open(inputFileName, 'r').readlines()
	for i in read_file:
		stack.push(i)
	return stack

def palindrome(Array_Stack):
	stack = da.Stack()
	reverse_stack = da.Stack()
	initial_list = []
	stack_list = []
	if not Array_Stack.isempty():
		pop = Array_Stack.pop()
		initial_list.append(pop)
		stack.push(pop)
	stack_list = initial_list[::-1]
	for i in stack_list:
		Array_Stack.push(i)
		stack.push(i)
	if stack == reverse_stack:
		return True
	else:
		return False

def reverse(Array_stack):
	our_list = da.Stack()
	the_list = []
	if not Array_stack.isempty():
		pop = Array_queue.pop() 
		the_list.append(pop)
	new_list = the_list[::-1]
	our_list.push(new_list)
	return our_list

def length_and_sum(array_Stack):
	sum_of_nums = 0
	count = 0
	our_list = []
	while not array_Stack.isempty():
		pop = array_Stack.pop()
		our_list.append(pop)
	for i in our_list:
		integer = int(i)
		count = len(our_list)
		sum_of_nums += integer
	return (count, sum_of_nums)

def main():
	our_stack = da.Stack()
	populate_obj = read_file(args.inputFileName, our_stack)
	#first_stack_copy = da.Queue()
	#second_stack_copy = da.Queue()
	#for i in range(len(our_stack)):
		#pop = our_stack[i]
		#first_stack_copy.push(pop)
		#second_stack_copy.push(pop)
	palindrome_yes = palindrome(populate_obj)
	print(palindrome_yes)
	reverse_stack = reverse(our_stack)
	palindrome_yes_yes = palindrome(reverse_stack)
	print(palindrome_yes_yes)
	print(populate_obj.front())
	print(length_and_sum(populate_obj))
	
if __name__=="__main__":
	main()










