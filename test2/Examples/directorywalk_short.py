import os
import hashlib
from datetime import datetime


def hash_file(filename):
    # make a hash object
    # the chance of a hash collision with sha1 or MD5 is minimal but I'm using sha256 because mem is plentiful
    h = hashlib.sha256()

    try:
        # open file for reading in binary mode - binary mode is a must
        with open(filename,'rb') as file:
            # loop till the end of the file
            fileChunk = None
            #while fileChunk != b'':
            while len(fileChunk) > 0:
                # read only 1024 bytes at a time
                #fileChunk = file.read(1024)
                # read only 4096 bytes at a time
                #fileChunk = file.read(4096)
                # read only 65536 bytes at a time
                fileChunk = file.read(65536)

                h.update(fileChunk)

        # the entire absolute path and file name
        print (os.path.realpath(file.name))
        # e.g exampe "/Users/michaelgeiser/PycharmProjects/test2/Examples/brianshirt_1.jpg"

        # return the hex representation of digest
        return h.hexdigest()

    except IOError as ioe:
        print("\n\nfile %s could not be opened" % filename)
        return "Error"

    finally:
        file.close()



startTime = datetime.now()
fileCounter = 0
#rootDir = '.'
rootDir = '/Users/michaelgeiser/Downloads'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)

    for fname in fileList:
        fileCounter += 1
        temp1 = str(fname) + ":" + str(hash_file(dirName+"/"+fname)) + " counter: " + str(fileCounter) + " : " + str(os.path.getsize(fname))
        #temp1 = str(fname) + ":" + " counter: " + str(fileCounter)
        print('\t%s' %  temp1 )

endTime = datetime.now()

totalTime = endTime - startTime
print ("Count of files hashed: " + str(fileCounter))
print ('Scanning Completed in: '+ str(totalTime))

