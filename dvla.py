import hashlib
import sys
import getopt
import os

# Main method
def main():
    inputDir = ''
    map = {}
    try: opts, args = getopt.getopt(sys.argv[1:], 'hi:', ['help', 'verbose', 'input='])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    output = None
    verbose = False
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    directory = get_directory(args);

    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file = os.path.join(root, name)
            assert os.path.exists(file)
            file_object = open(file, 'r')
            content = file_object.read()
            hash_object = hashlib.sha1(content)
            hex_dig = hash_object.hexdigest()
            if hex_dig not in map:
                map[hex_dig] = []
            map[hex_dig].append(file)

            # print 'Hash: ' + hex_dig + ' for ' + name
            # print(os.path.join(root, name))
        # for name in dirs:
            # print(os.path.join(root, name))
    for key in map:
        if len(map[key]) > 1:
            print 'These files are identical'
            for entry in map[key]:
                print '\t' + entry

def usage():
    print "Usage:"
    print "python dvla.py [--help] directory"

def get_directory(dir_names):
    dir_name = None;
    if len(dir_names) > 0:
        dir_name = os.path.abspath(dir_names[0])
        print dir_name
        if os.path.exists(dir_name) and os.path.isdir(dir_name):
            return dir_name
        else:
            assert False, dir_name + ' is either not a directory or does not exist!'
    else:
        assert False, 'no directory given to traverse'



if __name__ == "__main__":
    main()


# print sys.argv[1];
# if (len(sys))
# # print 'Number of arguments:', len(sys.argv), 'arguments.'
# # print 'Argument List:', str(sys.argv)
