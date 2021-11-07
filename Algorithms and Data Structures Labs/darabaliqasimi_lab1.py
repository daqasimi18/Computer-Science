def find_area(length, width):
    if length == None or width == None:
        return None
    return length * width

def find_volume(length, width, elevation):
    if length == None or width == None or elevation == None:
        return None
    return length * width * elevation

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type = int)
    parser.add_argument("-w", "--width", type = int)
    parser.add_argument("-e", "--elevation", type = int)
    args = parser.parse_args()
    
    new_volume = find_area(args.length, args.width), find_volume(args.length, args.width, args.elevation)
    print(new_volume)