char1, char2 = input("Enter two spaced-separated character: ").split()
max_char = max(char1, char2)

print("----------------------------")
print("The character with the greater value is:", max_char)
print("----------------------------")

print("Showing ASCII Value:")
print(f"{char1}:{ord(char1)}")
print(f"{char2}:{ord(char2)}")