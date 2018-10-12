"""

Fix the gotchas in the classes below.

"""

import uuid

class Person(object):
    """ A class representing a Person """
    
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(name):
        self.__name = name

        
class Employee(Person):
    """ An Employee class """

    eid = EmployeeID()
    
    def __init__(self, name):
        self._id = self.eid.get_id()
        super(Employee, self).__init__(name)

    def get_id(self):
        """ Return the employee id """
        
        return self._id

class EmployeeID(object):
    """ A class which makes a unique Employee system ID """
    
    def get_id(self):
        return uuid.uuid1().hex

if __name__ == "__main__":
    p = Person('Jack')
    p.set_name('Rock')
    e = Employee('Daniel')
    print e.get_id()
