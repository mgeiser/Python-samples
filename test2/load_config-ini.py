import ConfigParser

Config = ConfigParser.ConfigParser()

Config.read("configreadertest.ini")

print (Config.sections())

Name = ConfigSectionMap("SectionOne")['name']
Age = ConfigSectionMap("SectionOne")['age']
print "Hello %s. You are %s years old." % (Name, Age)



def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


