a = 0
b = 100


def sum_even(a, b):
    return sum(i for i in range(a, b + 1) if i % 2 == 0)
print(sum_even(a, b))
