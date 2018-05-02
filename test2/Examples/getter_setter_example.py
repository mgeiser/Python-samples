class Robot:

    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp
        self.__test = 123


    @property
    def condition(self):
        """
        defined using the @property decorator, you can assign condition

        for example:  you could use this line but it does nothing
        x.condition = 3

        """
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"


    @property
    def test(self):
        #return self.__test
        return "No"

    @condition.setter
    def condition(self, value):
        self.__test = value

    @condition.deleter
    def condition(self):
        del self.__test

    def set_potentials(self, potential_physical, potential_psychic):
        self.__potential_physical = potential_physical
        self.__potential_psychic = potential_psychic

    def __repr__(self):
        """
        __repr__ overrides the "representation" function that is the
        equivalent of the Java toString() method
        """
        return_string =  ("\n\n"+ "Robot Object" "\n"
            "Name: " + str(self.name) + "\n" 
            "Build Year: " + str(self.build_year) + "\n" 
            "Potential Physical: " + str(self.__potential_physical) + "\n" 
            "Potential Psychic: " + str(self.__potential_psychic) + "\n" )

        return return_string


if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)
    x.set_potentials(1,2)
    print(x.condition)

    # these all three print the equivalevnt of the Java toSting() in python
    # print(x)
    # print(str(x))
    # print(repr(x))

    print("\n\n\n")
    print("initial value of test: ")
    print(x.test)
    print("\nsetter called")
    x.test = 23  # setter called

    print("\ngetter called")
    print(x.test)   # getter called

    print("\ndeleter called")
    del x.test     # deleter called
    print(x.test)   # getter called


