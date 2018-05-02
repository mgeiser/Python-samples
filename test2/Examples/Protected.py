
#DTO getters and setters


# https://docs.python.org/3/library/exceptions.html


class Protective(object):
    def __init__(self, start_protected_value=0):
        self.protected_value = start_protected_value
    @property
    def protected_value(self):
        return self._protected_value
    @protected_value.setter
    def protected_value(self, value):
        #print("in setter")
        if value != int(value):
            raise TypeError("protected_value must be an integer")
        if 0 <= value <= 100:
            self._protected_value = int(value)
        else:
            raise ValueError("protected_value must be between 0 and 100 inclusive")
    @protected_value.deleter
    def protected_value(self):
        raise AttributeError("do not delete, protected_value can be set to 0")





p1 = Protective(3)
print( p1.protected_value)

p1 = Protective(5.0)
print(p1.protected_value)

try:
    p1 = Protective(-5)
except ValueError as ve:
    print("\n\n" + ve.message)


try:
    p1 = Protective(7.5)
except TypeError as te:
    print("\n\n" + te.message)


#p1 = Protective(7.5)

try:
    del p1.protected_value
except AttributeError as ae:
    print("\n\n" + ae.message)