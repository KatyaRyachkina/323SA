def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    return a * power(a, n - 1)


if __name__ == "__main__":
    print(power(2, 3))
    print(power(5, 0))
