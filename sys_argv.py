#!/usr/bin/python3
import sys
import getopt

name1 = sys.argv[1]
name2 = sys.argv[2]
name3 = sys.argv[3]

def myfunct(argv):
    if opt == '-h':
        print ("This is the -h")

    elif opt in ("-i", "--input"):
        arg_input = arg
    elif opt in ("-u", "--user");
        arg_user = arg
    elif opt in ("-o", "--output"):
        arg_output arg

def read_file(filename):
    with open(filename) as file:
        while True:
            line = file.readline()

            if len(line) == 0:
                break

            print(line)

files = sys.argv[1:]

for filename in files:
    read_file(filename)

print("hello", name1,",",name2," and ", name3)

