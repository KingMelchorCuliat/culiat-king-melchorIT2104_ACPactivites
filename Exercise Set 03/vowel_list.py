string = input("Enter a string: ")

vowels = "aeiouAEIOU"

vowel_list = [char for char in string if char in vowels]

print(vowel_list)