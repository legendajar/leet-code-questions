'''
    In this problem we have to find the container with most water. For example, given [1,8,6,2,5,4,8,3,7], the container with most water is 49.

    We solve this problem using two pointer approach.

    We use following step for solving this problem:

    1) First we have to initialize two variables 'left' and 'right' with value 0 and len(a) - 1 respectively.
    2) Then, we start a loop which continues until left < right.
    3) Then, we have to calculate the length of the container and the width of the container.
    4) Then, we have to calculate the total water.
    5) Then, we have to update the max water.
    6) If the value at left is less than the value at right then we increment left by 1. Otherwise, we decrement right by 1.
    7) Finally, we return the max water.
'''
def containerWithMostWater(a):
    left = 0
    right = len(a) - 1
    max_water = 0
    while left < right:
        length = min(a[left], a[right])
        width = right - left
        total_water = length * width
        max_water = max(max_water, total_water)

        if a[left] < a[right]:
            left += 1
        else:
            right -= 1
    return max_water

if __name__ == "__main__":
    a = [1,1]
    print(containerWithMostWater(a))