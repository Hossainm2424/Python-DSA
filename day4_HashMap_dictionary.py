# What is a HashMap (or Dictionary) in Python?
# hash map is a data structure that stores data in key-value pairs.
# In Python, a HashMap is implemented using the built-in dictionary data type.

frequency ={1:100, 2:200, 3:300, 4:400}
print(frequency[3])


# frequency count 
counts = {}
arr = [1,2,3,4,1,2,1,3,4,1,2,1,5,6,7,8,5,4,3,2,1]
for x in arr:
    counts[x] = counts.get(x,0) + 1

print("frequency of count",counts)

# Two sum - find two numbers that add up to a specific target

def two_Sum(arr, target):
    num_map = {}
    for i, num in enumerate(arr):
        # print("Current number:", num, i)
        diff = target - num
        if diff in num_map:
            return (diff, num)
        num_map[num] = i

arr = [2,7,11,15]
target = 9
result = two_Sum(arr, target)
print("Indices of numbers that add up to target:", result)



# contain duplicate 
def contain_duplicate(arr):
    num_set=set()
    for num in arr: 
        if num in num_set:
            return True
        num_set.add(num)
    return False

arr = [1,2,3,4,5,6,7,8,9]
print("Contain duplicate:", contain_duplicate(arr))

    


