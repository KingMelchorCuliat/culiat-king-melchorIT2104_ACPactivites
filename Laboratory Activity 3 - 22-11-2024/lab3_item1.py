def roman_to_integer(roman):
    roman_values = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000} 
    
    result = 0
    prev_value = 0
    
    for i in range(len(roman) - 1, -1, -1): 
        current_value = roman_values.get(roman[i])
        if current_value is None:
            return "Invalid Roman numeral"
        
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
            prev_value = current_value
    return result

def main():
    roman_numeral = input("Enter a Roman numeral: ").upper()
    
    integer_value = roman_to_integer(roman_numeral)
    print(f"The integer value of '{roman_numeral}' is:  {integer_value}")
    
if __name__ == "__main__":
    main()

    
   
    