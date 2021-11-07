
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFileName")
args = parser.parse_args()

def read_file(inputFileName):
	our_list = []
	addbooks = 0
	removebooks = 0
	checkouts = 0
	checkins = 0
	read = open(inputFileName, 'r').readlines()
	for i in read:
		split = i.split(',')
		our_list.append(split)
		split_keys = split[0]
		if split_keys == "addBook":
			addbooks += 1
		if split_keys == "removeBook":
			removebooks += 1
		if split_keys == "checkout":
			checkouts += 1
		if split_keys == "checkin":
			checkins += 1
		
	print(addbooks - removebooks)
	print(checkouts)
	print(checkins)
	return our_list

def most_often(our_list):
	new_list = []
	a_list = []
	b_list = []
	c_list = []
	for i in our_list:
		if i[0] == "addBook" or i[0] == "checkout" or i[0] == "checkin":
			new_list.append(i)
			checkouts = i
	for j in new_list:
		value = j[2].strip()
		a_list.append(value)
	most_freq = max(set(a_list), key = a_list.count).strip()
	for k in new_list:
		value_1 = k[1].strip()
		value_2 = k[2].strip()
		if most_freq == value_1 or most_freq == value_2:
			next_step = k
			b_list.append(next_step)
	popular_book = b_list[1]
	popular = popular_book[1], popular_book[2]
	count = 0
	for l in b_list:
		if l[0] == "checkin":
			count += 1
	print(popular, count)
	domain = b_list[0]
	count = 0
	for lines in b_list:
		curr_freq = b_list.count(lines)
		while curr_freq > count:
			count = curr_freq
			domain = lines[1]
	Count = count + 1
	print(domain, Count)

if __name__=="__main__":
	read = read_file(args.inputFileName)
	our_list = most_often(read)
	most_often(our_list)







