# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 

# which is the number of times you must multiply the digits in num until you reach a single digit.


def persistence(n):
    counter = 0
    while n > 9:
        counter += 1
        total = 1
        num_str = str(n)
        for digit in num_str:
            total = total * int(digit)
        n = total
    return counter
            
    
persistence(38)