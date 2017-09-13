import os
import sys

if len(sys.argv) != 3:
    print('Usage: python3 1:\ Searching\ in\ OS.py <location> <file / directory>')
else:
    object = sys.argv[2]
    print(object)
    found = 0
    if '*' in object:
        wildcard_index = object.index('*')
        for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
            for dir in dirnames:
                if wildcard_index == 0:
                    if dir.endswith(object[1:]):
                        print(os.path.join(dirpath, dir))
                        found += 1
                else:
                    if dir.startswith(object[-1:]):
                        print(os.path.join(dirpath, dir))
                        found += 1
            for file in filenames:
                if wildcard_index == 0:
                    if file.endswith(object[1:]):
                        print(os.path.join(dirpath, file))
                        found += 1
                else:
                    if file.startswith(object[-1:]):
                        print(os.path.join(dirpath, file))
                        found += 1
    else:
        for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
            if object in dirnames or object in filenames:
                print(os.path.join(dirpath, object))
                found += 1
    if found == 0:
        print('No such files found.')
    else:
        print('Found {} matches!'.format(found))