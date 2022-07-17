#!/usr/bin/python3
import sys
import getopt

args = sys.argv[1:]
arg_input = ''
arg_user = ''
arg_output = ''

n = len(sys.argv)
add = 0.0

try:
    opts, args = getopt.getopt(args, "hi:o:", ["--input", "--output"])
except getopt.GetoptError:
    print ("sys_argv.py --input <inputfile> --user <user_id> --output <outputfile>")
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
       print ("This is the -h switch")
       print ("sys_argv.py --input <inputfile> --user <user_id> --output <outputfile>")
       sys.exit()

   # python3 flags 
    if opt in ("-i", "--input"):
       arg_input = arg
       print ("Input file is ", arg_input)
    elif opt in ("-u", "--user"):
       arg_user = arg
       print ("User mod is ", arg_user)
    elif opt in ("-o", "--output"):
       arg_output = arg
       print ("Output file is ", arg_output) 
    elif opt in (n):
       for i in range(1, n):
        add += float(sys.argv[i])
        print ("The sum is :", add)

    # output options section URL
    # http://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/


    #print ("Input file is ", arg_input)
    # print ("User mod is ", arg_user)
    # print ("Output file is ", arg_output)
    #print ("The sum is :", add)

