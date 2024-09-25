def isPalindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")

number = int(input("Enter an integer: "))
isPalindrome(number)

