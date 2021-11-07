
def find_area(length, width):
	area = length * width
	return area


def find_volume(length, width, elevation):
	area = length * width
	volume = area * elevation
	return volume




if __name__=="__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--length", type = int)
	parser.add_argument("-w", "--width", type = int)
	parser.add_argument("-e", "--elevation", type = int)
	
	args = parser.parse_args()

	if args.length != None and args.width != None and args.elevation != None:
		volume = find_area(args.length, args.width), find_volume(args.length, args.width, args.elevation)
	if args.length != None and args.width != None and args.elevation == None:
		volume = find_area(args.length, args.width), None
	if args.length != None and args.width == None and args.elevation == None:
		volume = (None, None)

	print(volume)