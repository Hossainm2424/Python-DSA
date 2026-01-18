# What is time complexity? 
# Time complexity is how the runtime grow as the input zise increases. 

for element in range(1,11):
    print(element)
# The above code has a time complexity of O(n) because as the input size increases, the number of operations increases linearly.

# Big O Notations 
# O(1) - Constant Time: The runtime does not change with the size of the input data.
# O(log n) - Logarithmic Time: The runtime grows logarithmically as the input size increases.
# O(n) - Linear Time: The runtime grows linearly with the input size.
# O(n log n) - Linearithmic Time: The runtime grows in proportion to n log n.
# O(n^2) - Quadratic Time: The runtime grows quadratically with the input size.
# O(2^n) - Exponential Time: The runtime doubles with each additional element in the input data.

print("Example of O(1)")
# Example of O(n)
for e in range (1,5):
    print(e)


print("Example of O(n^2)")
# Example of O(n^2)
for i in range(1,5):
    for j in range(1,5):
        print(i, j)


print("Example of binary search O(log n)")
left=0
right=10
while left<=right:
    mid=(left+right)//2
    print(mid)
    left=mid+1
    right=mid-1



# Hash map lookup O(1)
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Example of hash map lookup O(1)")
print(my_dict["b"]) 


# Space Complexity - extra space or memory used. We count extra variables, data structure used, Recursion stack space etc.
