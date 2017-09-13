import os
import sys

if len(sys.argv) != 3:
    print('Usage: python3 1:\ Searching\ in\ OS.py <location> <file / directory>')
else:
    object = sys.argv[2]
    chars = list(object)
    found = 0
    for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
        if object in dirnames or object in filenames:
            print(os.path.join(dirpath, object))
            found += 1
    if found == 0:
        print('No such files found.')
    else:
        print('Found {} matches!'.format(found))