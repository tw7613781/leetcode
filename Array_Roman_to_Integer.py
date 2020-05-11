def romanToInt(s):
    rule2 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    rule1 = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900      
    }
    summation = 0
    is_special_case = False
    for index, char in enumerate(s):
        if not is_special_case:
            if index + 1 < len(s):
                temp = rule1.get(char + s[index + 1])
                if temp:
                    summation += temp
                    is_special_case = True
                else:
                    temp = rule2.get(char)
                    if temp: summation += temp
            else:
                temp = rule2.get(char)
                if temp: summation += temp                
        else:
            is_special_case = False
    return summation

assert(romanToInt('III') == 3)