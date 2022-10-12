class Number:
    def is_odd(n):  # static
        return n % 2 == 1

    def is_even(n):
        return n % 2 == 0


print(Number.is_even(7))
print(Number.is_even(24))
