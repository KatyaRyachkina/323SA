def power_v2(number, exponent=2):
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for i in range(exponent):
            result *= number
        return result
    else:
        return 1 / power_v2(number, -exponent)

print(power_v2(3, 3)) 
print(power_v2(5))     
print(power_v2(2, 4))
