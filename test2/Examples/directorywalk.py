import os
import hashlib
from datetime import datetime




def hash_file2(filename):
    # this thing
    try:
        openedFile = open(filename)
        readFile = openedFile.read()

        md5Hash = hashlib.md5(readFile)
        md5Hashed = md5Hash.hexdigest()

        sha1Hash = hashlib.sha1(readFile)
        sha1Hashed = sha1Hash.hexdigest()

        print ("File Name: %s" % filename)
        print ("MD5: %r" % md5Hashed)
        print ("SHA1: %r" % sha1Hashed)

    except IOError as ioe:
        print("\n\nfile %s could not be opened" % filename)
        return "Error"

    finally:
        openedFile.close()




def hash_file(filename):
    # https://www.programiz.com/python-programming/examples/hash-file
    #This function returns the SHA-1 has of the file passed into it

    # make a hash object
    # the chance of a hash collision with sha1 is minimal but I'm using sha256 because I can
    h = hashlib.sha256()

    try:
        # open file for reading in binary mode
        with open(filename,'rb') as file:
            # loop till the end of the file
            fileChunk = 0
            while fileChunk != b'':
            #while len(fileChunk) > 0:
                # read only 1024 bytes at a time
                #fileChunk = file.read(1024)
                # read only 4096 bytes at a time
                #fileChunk = file.read(4096)
                # read only 65536 bytes at a time
                fileChunk = file.read(65536)

                h.update(fileChunk)

        # just the file name
        #print (file.name)
        # the entire absolute path and file name
        print (os.path.realpath(file.name))
        # e.g would return "/Users/michaelgeiser/PycharmProjects/test2/Examples/brianshirt_1.jpg"

        # return the hex representation of digest
        return h.hexdigest()
        #return "test"

    except IOError as ioe:
        print("\n\nfile %s could not be opened" % filename)
        return "Error"

    finally:
        file.close()



def hash_file3(filename):
    # make a hash object
    # the chance of a hash collision with sha1 is minimal but I'm using sha256 because I can
    h = hashlib.sha256()

    h.update("test")
    return h.hexdigest()
    #return "test"






startTime = datetime.now()
fileCounter = 0
#rootDir = '.'
rootDir = '/Users/michaelgeiser/Downloads'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)

    for fname in fileList:
        fileCounter += 1
        temp1 = str(fileCounter) + "   :   " + str(fname) + ":" + str(hash_file(dirName+"/"+fname)) + " File Length: " + str(os.path.getsize(dirName+"/"+fname))
        #temp1 = str(fname) + ":" + " counter: " + str(fileCounter)
        print('\t%s' %  temp1 )

endTime = datetime.now()

totalTime = endTime - startTime
print ("Count of files hashed: " + str(fileCounter))
print ('Scanning Completed in: '+ str(totalTime))

