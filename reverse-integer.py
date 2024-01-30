'''
    In this question we have to reverse an integer.
    For example, given 123, you should return 321.

    We are using the following steps to solve this problem:
    1) Firstly, we need to declare the int_max and int_min variables.
    2) Then, we need to check if the number is negative or not. If it's negative then we convert it into positive by multiplying with -1.
    3) Then, we need to initialize the result variable to 0.
    4) After that, we will check if our input number is negative or positive. If it's negative then we will multiply it with -1.
    5) Then, we will use while loop to reverse the number. If x is greater than zero then we add x%10 to the result and subtract the result by 10.
    6) Finally, we will return the result.

'''
def reverseInteger(x):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    result = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)

    while x > 0:
        digit = x % 10
        # Check for integer overflow
        if result > (INT_MAX - digit) // 10:
            return 0
        result = result * 10 + digit
        x //= 10

    return sign * result

if __name__ == "__main__":
    x = int(input("Enter number: "))
    print(reverseInteger(x))