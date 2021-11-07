import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFileName")
args = parser.parse_args()

class Node:
    def __init__(self, domain):
    	self.domain = domain
    	self.left_child = None
    	self.right_child = None
    	self.count = 1

class binary_search_tree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, domains):
        if self.root is None:
            self.root = Node(domains)
        current_node = self.root
        while current_node is not None:
            if current_node.domain == Node(domains).domain:
                current_node.count += 1
                return
            elif current_node.domain > Node(domains).domain:
                if current_node.left_child is None:
                    current_node.left_child = Node(domains)
                    return
                else:
                    current_node = current_node.left_child
            else:
                if current_node.right_child is None:
                    current_node.right_child = Node(domains)
                    return
                else:
                    current_node = current_node.right_child

def read_file(inputFileName):
    our_list = binary_search_tree()
    file_open = open(inputFileName,"r").readlines()
    for i in file_open:
        split_line = i.split(":")
        index_zero = split_line[0]
        our_list.insert(index_zero)
    return our_list

def print_tree(domains):
    if domains is not None:
        print_tree(domains.left_child)
        print(domains.domain, domains.count)
        print_tree(domains.right_child)

def main():
    our_list = read_file(args.inputFileName)
    print_tree(our_list.root)


if __name__=="__main__":
    main()