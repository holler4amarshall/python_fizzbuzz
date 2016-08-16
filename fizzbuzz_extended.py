import sys

try:
    if int((sys.argv[1])) > 0:
        number = int((sys.argv[1]))
        print 'sys arg number = ' + str(number)

    # here, I tried to put in an else statement to capture user input, but could never get it to work.... so split it into a strange nested try / except

except:
    try:
        num = input("Please enter a whole number: ")
        print "num = " + str(num)
        number = int(num)
    except:
        print "invalid number entered"

def fizz_buzz(number):

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