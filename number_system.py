def dec2bin(number):
    return dec_to(number, 2)

def dec2oct(number):
    return dec_to(number, 8)

def dec2hex(number):
    return dec_to(number, 16)



def bin2dec(number):
    return to_dec(number, 2)

def oct2dec(number):
    return to_dec(number, 8)

def hex2dec(number):
    return to_dec(number, 16)

def dec_to(number, syst):
    result = []
    rest = 0
    letters={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    while number > syst - 1:
        rest = number % syst
        number = number // syst
        if syst == 16 and 10 <= rest <= 15:
            rest = letters.get(rest)
        result.insert(0, str(rest))
    if syst == 16 and 10 <= number <= 15:
        result.insert(0, str(letters.get (number)))
    else:
        result.insert(0, str(number))
    result = ''.join(result)
    return result


def to_dec(number, syst):
    j=1
    result=0
    letters={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    for i in number:
        if syst == 16 and letters.get(i) != None:
            i = letters.get(i)
        i = int(i) * (syst**(len(number)-j))
        j += 1
        result= result + i
    return result

print(dec2bin(24584), type (dec2bin))
