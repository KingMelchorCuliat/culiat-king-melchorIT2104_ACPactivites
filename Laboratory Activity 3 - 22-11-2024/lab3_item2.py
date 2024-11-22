def perfect_number(number):
    sum = 0
    for i in range (1, number):
        if number % i == 0:
            sum += i
    return sum == number

try:
    number = int(input("Enter a number: "))

    if perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")
except ValueError:
    print("Please enter a valid integer.")
