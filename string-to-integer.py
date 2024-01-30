'''
    In this question we have to convert a string to an integer. For example, given "123", you should return 123.

    We are using the following steps to solve this problem:
    1) Firstly, we need to check if the string is empty or not. If it's empty then we return 0.
    2) Next, we will initialize a variable 'max_length' with value 0
'''

def stringToInteger(s):
        s = s.strip()
    
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        result = sign * result

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = min(max(result, INT_MIN), INT_MAX)
        return result

if __name__ == "__main__":
    s = input("Enter String: ")
    print(stringToInteger(s))