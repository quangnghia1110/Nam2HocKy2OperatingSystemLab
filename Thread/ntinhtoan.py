import threading

average_value = 0
minimum_value = 0
maximum_value = 0

def calculate_average(numbers):
    global average_value
    average_value = sum(numbers) / len(numbers)

def calculate_minimum(numbers):
    global minimum_value
    minimum_value = min(numbers)

def calculate_maximum(numbers):
    global maximum_value
    maximum_value = max(numbers)

if __name__ == '__main__':
    numbers = list(map(int, input("Enter numbers: ").split()))
    average = threading.Thread(target=calculate_average, args=(numbers,))
    mininum = threading.Thread(target=calculate_minimum, args=(numbers,))
    maxinum = threading.Thread(target=calculate_maximum, args=(numbers,))
    average.start()  
    average.join()
    mininum.start()
    mininum.join()
    maxinum.start()
    maxinum.join()
    print(f'The average value is {average_value}')
    print(f'The minimum value is {minimum_value}')
    print(f'The maximum value is {maximum_value}')
    
