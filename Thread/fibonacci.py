import threading

MAX = 100
fibonacci_value = [0] * MAX

def calculate_fibonacci(n):
    fibonacci_value[0] = 0
    fibonacci_value[1] = 1
    for i in range(2, n):
        fibonacci_value[i] = fibonacci_value[i-1] + fibonacci_value[i-2]

if __name__ == "__main__":
    n = int(input("Enter the number: "))   
    fibonacci = threading.Thread(target=calculate_fibonacci, args=(n,))
    fibonacci.start()
    fibonacci.join()
    print(fibonacci_value[:n])