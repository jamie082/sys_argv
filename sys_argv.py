#!/usr/bin/python3
import sys
import getopt

def main():

    try:
        opts, args = getopt.getopt(args, "hi:o:", ["--input", "--output"])
    except getopt.GetoptError:
        print ("sys_argv.py --input <inputfile> --user <user_id> --output <outputfile>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ("sys_argv.py --input <inputfile> --user <user_id> --output <outputfile>")
            print ("This is the -h")
            sys.exit()

        elif opt in ("-i", "--input"):
            arg_input = arg
        elif opt in ("-u", "--user"):
            arg_user = arg
        elif opt in ("-o", "--output"):
            arg_output = arg

"""
print("hello", name1,',',name2,' and ', name3)


myfunct(sys.argv)
