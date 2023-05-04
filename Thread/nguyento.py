import threading

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    t = threading.Thread(target=print_primes, args=(n,))
    t.start()
    t.join()

