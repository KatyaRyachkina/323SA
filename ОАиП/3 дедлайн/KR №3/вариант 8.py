def _power_factory(exponent):
    def power_function(x):
        return x ** exponent
    return power_function

class MathTools:
    @classmethod
    def create_power_list(cls, numbers, n):
        power_func = _power_factory(n)
        return [power_func(num) for num in numbers]

if __name__ == "__main__":
    square = _power_factory(2)
    print("square(3) =", square(3))
    
    numbers = [1, 2, 3, 4]
    result = MathTools.create_power_list(numbers, 3)
    print("Кубы", numbers, ":", result)
