name = 'Zed A. Shaw'
age = 35 # not a lie
heigth = 74 #inches
weigth = 180 #lbs
eyes = 'Brown'
teeth = 'yellow'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % heigth
print "He's %d pounds heavy." % weigth
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffe." % teeth

#this line is tricky, try to get it exactly right
print "If I add %r, %d, and %d I get %d." % (age, heigth, weigth, age + heigth + weigth)
