def letterValue(l):
    '''
    Takes parameter of type str and returns the corresponding value of the string
    The string must be a letter from A to F
    '''
    if l == 'A':
        return 10
    if l == 'B':
        return 11
    if l == 'C':
        return 12
    if l == 'D':
        return 13
    if l == 'E':
        return 14
    if l == 'F':
        return 15

def valueToLetter(v):
    '''
    Takes parameter of type int and returns the corresponding letter of the value
    The string must be a number from 10 to 15
    '''
    if v == 10:
        return 'A'
    if v == 11:
        return 'B'
    if v == 12:
        return 'C'
    if v == 13:
        return 'D'
    if v == 14:
        return 'E'
    if v == 15:
        return 'F'

def base10(base,num):
    '''
    Gets the type int base and type str number and returns the number in base 10 as a type str
    '''
    p = -1 # power 
    decimal = 0 #stores converted base 10 number
    #Finds the power of the most significant bit
    for i in num:
        if i == '-':
            pass
        elif i == '.':
            break
        else:
            p +=1
    #converts the number into base 10
    for i in num:
        if i == '.' or i == '-':
            pass
        elif 'A' <= i <= 'F':
            decimal += letterValue(i) * base**(p)
            p -= 1
        else:
            decimal += int(i) * base**(p)
            p -= 1
    return str(decimal)

def convert(base,num):
    '''
    Gets the type int base and type str number and returns a type str of the number converted to another base
    The base is the base the number will be converted to and the number must be in base 10
    '''
    temp = '' #stores string of the integer portion of the number
    quotient = 0 #stores integer portion of number
    decimal = 0 #stores decimal portion of number
    #if the number is a floating point number then the integer is separated from the decimal portion
    if '.' in num:
        #stores integer portion into 'quotient' variable and decimal portion in 'decimal' variable
        for i in range(len(num)):
            if num[i] == '.':
                quotient = int(temp)
                decimal += float(num[i:])
                break
            temp += num[i]
    #stores number in 'quotient' variable
    else:
        for i in range(len(num)):
            temp += num[i]
        quotient = int(temp)
    result = ''
    #determines integer portion of the result
    while quotient > 0:
        remainder = quotient % base
        quotient = quotient // base
        #concatenates corresponding letter to 'result' for numbers greater than or equal to 10
        if remainder >= 10:
            result = str(valueToLetter(remainder)) + result
        #otherwise concatenates the remainder to 'result'
        else:
            result = str(remainder) + result
    #adds decimal to result if the number was a floating point number
    if '.' in num:
        result += '.'
    count = 1
    #determines decimal portion of the result for up to 10 digits
    while decimal > 0:
        if count == 10:
            break
        decimal *= base
        if decimal >= 10:
            result += str(valueToLetter(int(decimal)))
        else:
            result += str(int(decimal))
        decimal -= int(decimal)
        count += 1
    return result

if __name__ == "__main__":
    print('This program is a base converter for numbers in bases 2 to 16 inclusively.\n'+'-'*50)
    base1 = int(input('Enter the base of the number you will be inputting: '))
    #checks if the base is from 2 to 16
    while base1 < 2 or base1 > 16:
        base1 = int(input('The base entered was not between 2 to 16 inclusively, try again: '))
    num = input('Enter the number you want to convert: ').upper()
    #check if the number inputted is in the right base
    while True:
        #valid is true when the number entered is in the correct base
        valid = True
        #compares the value of each digit with the base to see if its not valid
        for i in num:
            if i == '.' or i == '-':
                pass
            elif 'A' <= i <= 'F':
                if letterValue(i) >= base1:
                    valid = False
            else:
                if int(i) >= base1:
                    valid = False
        #breaks the loop when a valid number is entered
        if valid:
            break
        #asks user to reenter the number
        else:
            num = input('Your entry was not in the correct base. Enter a new number: ').upper()
    base2 = int(input('Enter the base you want to convert your number to: '))
    #checks if the base is from 2 to 16
    while base2 < 2 or base2 > 16:
        base2 = int(input('The base entered was not between 2 to 16 inclusively, try again: '))
    print('-'*50)
    #converts the number to base 10 and then to the specified base2 from the user
    s1 = base10(base1,num)
    s2 = convert(base2,s1)
    if '-' in num:
        s2 = '-' + s2
    print(f'{num} in base {base1} is {s2} in base {base2}.')

