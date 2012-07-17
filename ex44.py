class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT overrider()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

    def override(self):
        print "CHILD overrider()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
    

dad = Parent()
son = Child()

print ".:: Implicit Inheritance ::."
print "\n"

dad.implicit()
son.implicit()

print "\n"
print ".:: Override Explicitly ::."
print "\n"

dad.override()
son.override()

print "\n"
print ".:: Alter Before Or Afte ::."
print "\n"

dad.altered()
son.altered()
