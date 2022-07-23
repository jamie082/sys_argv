#!/usr/bin/python3
import sys
import getopt

args = sys.argv[1:]
arg_input = ''
arg_user = ''
arg_output = ''

add = 0.0
n = len(sys.argv)
try:
    opts, args = getopt.getopt(args, "hi:u:o:-d", ["--input", "--user", "--output"])
except getopt.GetoptError:
    print ("sys_argv.py --input <inputfile> --user <user_id> --output <outputfile>")
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
       print ("This is the -h switch")
       print ("sys_argv.py --input <inputfile> --user <user_id> --output <outputfile>")
       sys.exit()

    if opt in ("-i", "--input"):
       arg_input = arg
       print ("Input file is ", arg_input)
    elif opt in ("-u", "--user"):
       arg_user = arg
       print ("User id is ", arg_user)
    elif opt in ("-o", "--output"):
       arg_output = arg
       print ("Output file is ", arg_output)

for i in range(1, n):
    add += float(sys.argv[i])
print("The sum is: ", add)
