def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_list(arr):
    arr = list(filter(lambda x: is_prime(x), arr))
    print(arr)

n = 100
arr1 = []
for i in range(1, n):
    arr1.append(i)

filter_list(arr1)
