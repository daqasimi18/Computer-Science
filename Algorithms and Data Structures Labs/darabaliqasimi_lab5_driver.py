import sys
import os.path
import dynamic_array as da

def creates_and_populates(inputFileName):
  populated_list = da.DynamicArray()
  read_file = open(inputFileName, 'r').readlines()
  for lines in read_file:
    strip = lines.strip()
    populated_list.append(int(strip))
  return populated_list

def unique_objects(populated_list):
  unique_list = []
  for i in populated_list:
    if i not in unique_list:
      unique_list.append(i)
  return unique_list

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description='Lab 5 - arrays')
	parser.add_argument('-i','--inputFileName', type=str, help='File of integers, one per line', required=True)
	args = parser.parse_args()

	if not (os.path.isfile(args.inputFileName)):
		print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
		exit(-1)

	myArray = da.DynamicArray()
	myArray = creates_and_populates(args.inputFileName)
	unique_1 = unique_objects(myArray)
	for i in range(len(unique_1)):
	  print(unique_1[i])
	print(myArray[-15])
	myArray.remove_all(7)
	print(myArray[-15])
	


	




	