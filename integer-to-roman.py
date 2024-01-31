'''
    In thi problem we have to convert an integer into roman number.
    Input: 12
    Output: XII

    We can solve this problem using the following steps:
    1) First we have to initialize a variable 'roman' with an empty string. This will be used to store our final result.
    2) Then we have to initialize a list 'values' with values 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1. This will be used to store the values of each roman numeral.
    3) Then we have to initialize a list 'symbols' with symbols "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I". This will be used to store the symbols of each roman numeral.
    4) Then we have to use a while loop to convert the integer into roman numeral.
        - If the input is less than or equal to 0, then return empty string.
        - Initialize an empty string called "result" which will store our final result.
        - While the input is greater than 0, do the following:
            - Take modulo of the input with 10 and assign it to variable 'remainder'.
            - If 'remainder' is 0, then append the corresponding symbol to 'result'.
                - For value = 10, symbol = "X".
                - For value = 9, symbol = "IX".
                - For value = 8, symbol = "V".
                - For value = 7, symbol = "VI".
                - For value = 6, symbol = "IV".
                - For value = 5, symbol = "V".
            - Divide the input by 10 and take floor division (//=). This will remove the last digit from the input.
        
    5) Finally, return the 'roman' variable.
'''

def intToRoman(num):
    roman = ''
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman += symbols[i]
            num -= values[i]
        i += 1
    return roman


if __name__ == "__main__":
    num = int(input("Enter number: "))
    print(intToRoman(num))