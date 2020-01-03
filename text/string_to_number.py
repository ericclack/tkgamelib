def single_digit(s):
    return ord(s) - ord('0')

def mult_digit(s):
    if len(s) == 1:
        return single_digit(s)
    else:
        return single_digit(s[-1]) + (10 * mult_digit(s[:-1]))

def mult2_digit(s):
    total = 0
    for i in range(len(s)):
        total += int(s[i]) * (10**(len(s)-i-1))
    return total
    
print(single_digit('0'))
print(mult_digit('51'))
print(mult2_digit('521'))

# 1 + 10*2 + 10*10*5
