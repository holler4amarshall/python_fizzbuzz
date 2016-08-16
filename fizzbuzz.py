def fizz_buzz(N):
    result = ''
    fizz = ''
    print 'Fizz Buzz counting up to ' + str(N)
    for item in range(1, N + 1):
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


fizz_buzz(100)