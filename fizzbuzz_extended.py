import sys

try:
    if int((sys.argv[1])) > 0:
        number = int((sys.argv[1]))
        print 'sys arg number = ' + str(number)

    # possibly move the input() here, as an else statement.

except:
    try:
        num = input("Please enter a whole number: ")
        print "num = " + str(num)
        number = int(num)
    except:
        print "invalid number entered"

def fizz_buzz(number):
    """print range of numbers from 1 to user defined number. if number divisible by 3, print fizz.
    if number divisible by 5, print buzz. if number divisible by both, print fizzbuzz."""

    result = ''
    print 'Fizz Buzz counting up to ' + str(number)
    for item in range(1, number + 1):
        if item % 3 != 0 and item % 5 != 0:
            result = item
        else:
            #reset result to blank value, if it is not an integer non divisible by 3 or 5
            result = ''
            if int(item) % 3 == 0:
                result = str(result) + 'Fizz'
            if item % 5 == 0:
                result = str(result) + 'Buzz'
        print result

fizz_buzz(number)