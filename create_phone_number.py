# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

#Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    f = "".join(map(str, n[:3]))
    s = "".join(map(str, n[3:6]))
    t = "".join(map(str, n[6:10]))
    return "({}) {}-{}".format(f,s,t)

myNumber = [8,6,0,7,5,1,2,6,8,7]

print(create_phone_number(myNumber))



