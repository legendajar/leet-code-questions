'''
In this question we have to convert a string into zigzag format according to the number of rows we want.

For example, if we have 3 rows we have to convert the string into the following format.
"PAYPALISHIRING" is the input string.
If we print it as ZigZag pattern you will get:
PAHNAPLSIIGYIR

We are using the following steps to solve this problem:

1) Firstly, we need to initialize an empty 2D array with the given number of rows.
2) Then, we need to use the list of numbers from 0 to numRows - 1 and the list of numbers from 0 to numRows - 1 to create the zigzag pattern.
3) Then, we need to use the list of numbers from 0 to numRows - 1 to create the zigzag pattern. In our case, there are 3 rows so we use the list of numbers from 0 to 2 to create the zigzag pattern.
4) Finally, we need to use the list of numbers from 0 to numRows - 1 to create the zigzag pattern. In our case, there are 3 rows so we use the list of numbers from 0 to 2 to create the zigzag pattern.
'''

def zigzagConversion(string, numRows):
    t = list(range(numRows)) + list(range(numRows - 2, 0, -1))

    r = [''] * numRows

    for i, char in enumerate(string):
        r[t[i % len(t)]] += char

    return ''.join(r)

if __name__ == "__main__":
    string = input("Enter String: ")
    numRows = int(input("Enter Number of Rows: "))
    print(zigzagConversion(string, numRows))