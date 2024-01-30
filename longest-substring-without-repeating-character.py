# Program to find the longest substring without repeating character
# In this program we have given a string and we have to find the longest substring without repeating character in a string

'''
We solve this question using sliding window approach

Following steps are used to solve this problem:-

1. First we have to create an empty dictionary and initialize i = 0 and result = 0
2. Then we have traverse j from 0 to len(string) - 1 (i.e., for each character in string).
3. Then we have to check if the current character is present in dictionary or not, if yes then we have to update the index of i to max(i, visited[string[j]]) and if not then we have to update the dictionary with key as string[j] and value as j + 1 and also update the result to max(result, j - i + 1).
4. Finally we have to return result

'''

def longestSubstringWithoutRepeatingCharacter(string):
    visited = {}
    i = 0
    result = 0

    for j in range(len(string)):
        if string[j] in visited:
            i = max(i, visited[string[j]])
        visited[string[j]] = j + 1
        result = max(result, j - i + 1)
    return result


if __name__ == "__main__":
    string = input("Enter String: ")
    print(longestSubstringWithoutRepeatingCharacter(string))