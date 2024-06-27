def normal_print(numbers):
    for i in numbers:
        print(f'{i}    ',end='')
    print()

def reverse_print(numbers):
    for i in numbers[::-1]:
        print(f'{i}    ',end='')
    print()

def sum_print(numbers):
    sum_n = 0
    for i in numbers:
        sum_n += i
    return sum_n

def average_print(numbers):
    sum_n = sum_print(numbers)
    total = len(numbers)
    average = sum_n/total
    return average
    
numbers = []

for i in range(8):
    numbers.append(float(input('Enter number '+str(i +1)+": ")))

print()
normal_print(numbers)
reverse_print(numbers)
print('Sum of numbers: '+str(round(sum_print(numbers),2)))
print('Average of numbers: '+str(round(average_print(numbers),2)))
print('The numbers above average are: ',end='')
for i in numbers:
        if i > average_print(numbers):
            print(f'{i}    ',end='')