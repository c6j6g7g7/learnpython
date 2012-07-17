
numbers = []

def print_numbers(maximum=4, increment=1):
    print maximum, increment
    i = 0
    for i in range(i,maximum):
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print_numbers(3, 2)

print "The numbers: "

for num in numbers:
    print num
