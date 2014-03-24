the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count", number

# same as above
for fruit in fruits:
    print "A fruit of type: ", fruit

# This loop has an 'if' clause
for fruit in fruits:
    if 'ap' in fruit:
        print fruit