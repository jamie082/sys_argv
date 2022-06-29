#!/usr/bin/python3
import sys, getopt

def main():
    if opt == '-h':
        print ("This is the -h")

    name1 = sys.argv[1]
    name2 = sys.argv[2]
    name3 = sys.argv[3]

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

