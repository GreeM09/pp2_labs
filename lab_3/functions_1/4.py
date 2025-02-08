def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
            return False
    return True

def filter_list(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
prime_numbers = filter_list(numbers)
print("Prime numbers:", prime_numbers)

