import argparse
import copy

parser = argparse.ArgumentParser()
parser.add_argument("-i","--inputFileName")
args = parser.parse_args()

class stack:
    def __init__(self):
        self._stack=[]
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

def read_file(inputFileName, Stack):
	read_file = open(inputFileName, 'r').readlines()
	for i in read_file:
		Stack.push(i)
	return Stack

def palindrome(Array_Stack):
	Stack = stack()
	reverse_stack = stack()
	initial_list = []
	stack_list = []
	if not Array_Stack.isempty():
		pop = Array_Stack.pop()
		initial_list.append(pop)
		Stack.push(pop)
	stack_list = initial_list[::-1]
	for i in stack_list:
		Array_Stack.push(i)
		Stack.push(i)
	if Stack == reverse_stack:
		return True
	else:
		return False

def reverse(Array_stack):
	our_list = stack()
	the_list = []
	if not Array_stack.isempty():
		pop = Array_stack.pop() 
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
	our_stack = stack()
	populate_obj = read_file(args.inputFileName, our_stack)
	copy_stack = copy.deepcopy(our_stack)
	palindrome_yes = palindrome(populate_obj)
	print(palindrome_yes)
	reverse_stack = reverse(our_stack)
	palindrome_yes_yes = palindrome(reverse_stack)
	print(palindrome_yes_yes)
	print(populate_obj.top())
	print(length_and_sum(our_stack))
if __name__=="__main__":
	main()










