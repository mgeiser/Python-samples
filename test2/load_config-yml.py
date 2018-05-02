# You will need to first do a "sudo pip install pyyaml"
# Menu PyCharm - Preferences - Project - Project Intrpreter - add the package


import yaml
from decimal import *





configFileName = "configreadertest.yml"

try:
    with open(configFileName, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

        #for section in cfg:
        #    print(section)

        username = cfg['mysql']['user']


        test = Decimal("0.1")
        print (test)
        print ("\n\nDecimal Usage")
        print ("%d = 0.3"  %(test + test + test))
        print ((test+test+test == Decimal(0.3)))
        print {"\n\n\n"}


        for directories in cfg['directories']:
            print directories
        print "\n\n"
        for behaviors in cfg['behavior']:
            print behaviors

        print cfg['behavior']['delete_checked_file_if_dup']

        newFilesDirectory = cfg['directories']['new_files_directory']
        fileToCheckDirectory  = cfg['directories']['files_to_check_directory']
        fileRepoRootDirectory = cfg['directories']['file_repo_root_directory']



        test = cfg["other"]["preprocessing_queue"][0]
        print "\n\n"
        for answer in cfg["other"]["preprocessing_queue"]:
            print (answer)

        print ("\n\n\n" + test)





except IOError as ioe:
    print(ioe.message)
    #print("File " + configFileName +" not found")
    print("File %s not found" % configFileName)

except Exception as ex:
    print("<p>Error: %s</p>" % ex)







