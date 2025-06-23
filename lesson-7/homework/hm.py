def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(13))

def digit_sum(k):
    s = 0
    while k > 0:
        s = s + (k % 10)
        k = k // 10
    return s
print(digit_sum(723251))

def print_powers_of_two(N):
    power = 1
    while power * 2 <= N:
        power *= 2
        print(power, end=' ')
print(print_powers_of_two(1))
