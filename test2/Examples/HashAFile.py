# Python program to find the SHA-1 message digest of a file

# import hashlib module
import hashlib
import os

def hash_file(filename):
    #This function returns the SHA-1 has of the file passed into it

    # make a hash object
    # the chance of a hash collision with sha1 is minimal but I'm using sha256 because I can
    h = hashlib.sha256()

    try:
        # open file for reading in binary mode
        with open(filename,'rb') as file:

            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)

        # just the file name
        #print (file.name)
        # the entire absolute path and file name
        print (os.path.realpath(file.name))
        # e.g woudl return "/Users/michaelgeiser/PycharmProjects/test2/Examples/brianshirt_1.jpg"


        # return the hex representation of digest
        return h.hexdigest()



    except IOError as ioe:
        print("\n\nfile %s could not be opened" % filename)
        return "Error"




#message = hash_file("../configreadertest.ini")
#print(message)

hash1 = hash_file("brianshirt_1.jpg")
hash2 = hash_file("brianshirt_2.jpg")

if (hash1==hash2):
    print("match")
else:
    print("no match")


