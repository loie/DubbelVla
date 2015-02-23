import hashlib
import sys
import getopt

def main():
    inputDir = ''
    verbose = False
    try: opts, args = getopt.getopt(sys.argv[1:], 'vhi:', ['help', 'verbose', 'input='])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    output = None
    verbose = False
    for o, a in opts:
        if v == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()

        else:
            assert False, "unhandled option"

def usage():
    print "Usage"

if __name__ == "__main__":
    main()


# try:
#     opts, args = getopt.getopt(argv,"hi:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print 'test.py -i <inputfile> -o <outputfile>'
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print 'test.py -i <inputfile> -o <outputfile>'
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg

#    print 'Input file is "', inputfile
#    print 'Output file is "', outputfile

# if __name__ == "__main__":
#    main(sys.argv[1:])


# print sys.argv[1];
# if (len(sys))
# # print 'Number of arguments:', len(sys.argv), 'arguments.'
# # print 'Argument List:', str(sys.argv)

# hash_object = hashlib.sha1(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)