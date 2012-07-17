from sys import argv

#unpack arguments
script, filename = argv

#Open file with the name arguments
txt = open(filename)

#print name of file
print "Here's your file %r:" % filename
#print content file
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

#open file especificaded in the input text for user.
txt_again = open(file_again)

# print file especified for user.
print txt_again.read()

txt_again.close()
