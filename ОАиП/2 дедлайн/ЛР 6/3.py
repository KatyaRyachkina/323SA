def power_v2(number, exponent=2):
    """Функция возводит число в степень (по умолчанию в квадрат)"""
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for i in range(exponent):
            result *= number
        return result
    else:
return 1 / power_v2(number, -exponent)
print(power(3, 3)) 
print(power(5))     
print(power(2, 4))  
