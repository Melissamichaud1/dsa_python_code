def decimalToBinary(n):
    assert int(n) == n, "The param must be an integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(1.1))
