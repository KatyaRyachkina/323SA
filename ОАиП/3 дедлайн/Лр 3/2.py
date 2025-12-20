def sum_digits(number: int) -> int:
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)


if __name__ == "__main__":
    print(sum_digits(12345))
