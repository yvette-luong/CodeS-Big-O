'''
Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]
Notes:

Each input will have exactly one solution.
You may not use the same element twice.
[execution time limit] 4 seconds (py3)

[input] array.integer numbers

[input] integer target

[output] array.integer

- Input:
numbers: [3, 8, 12, 16]
target: 11
Expected Output:
[0, 1]

- Input:
numbers: [0, 1, 2, 3, 4, 5, 6, 7]
target: 13
Expected Output:
[6, 7]

- Input:
numbers: [3, 4, 5]
target: 8
Expected Output:
[0, 2]
'''

def csSortedTwoSum(numbers, target):    
#  i is the first number
#  j is the second number
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]   

print(csSortedTwoSum([3, 8, 12, 16], 11))
print(csSortedTwoSum([0, 1, 2, 3, 4, 5, 6, 7], 13))
print(csSortedTwoSum( [3, 4, 5], 8))